# Importa elementos necesarios de Flask y otros módulos
from . import auth_bp

import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for, session, redirect
)

from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

# Define una ruta '/register' bajo el Blueprint 'auth_bp' con métodos GET y POST
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Maneja el registro de nuevos usuarios.

    Returns:
        Redirige a la vista de login ('auth.login') si el registro es exitoso.
    """
    if request.method == 'POST':
        # Obtiene datos del formulario
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        db, c = get_db()
        error = None

        # Verifica si el nombre de usuario ya está registrado
        c.execute(
            'select id from users where username = %s', (username,)
        ) 
        if not username:
            error = 'Username es requerido'
        if not password:
            error = 'Password es requerido'
        elif c.fetchone() is not None:
            error = f'Usuario {username} se encuentra registrado'

        # Imprime la contraseña hasheada (para depuración)
        print(generate_password_hash(password))

        if error is None:
            # Inserta el nuevo usuario en la base de datos
            c.execute(
                'insert into users (username, email, password ) values (%s, %s, %s)',
                (username, email, generate_password_hash(password))
            )
            db.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


# Define una ruta '/login' bajo el Blueprint 'auth_bp' con métodos GET y POST
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Gestiona el logeo del usuario

    Returns:
        En caso que el login sea exitoso returna la plantilla de index.
    """
    if request.method == 'POST':
        # Obtiene datos del formulario
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        
        # Consulta la base de datos para verificar el usuario y la contraseña
        # Crear una funcion aparte que devuelva true o false
        c.execute(
            'select * from users where username = %s', (username,) 
        )
        user = c.fetchone()
        
        if user is None:
            error = 'User y/o password inválido'
        elif not check_password_hash(user['password'], password):
            error = 'User y/o password inválido'
        
        if error is None:
            # Limpia la sesión y establece el ID del usuario autenticado
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')

# Registra una función para ejecutarse antes de cada solicitud a la aplicación
@auth_bp.before_app_request
def load_logged_in_user():
    """
    Carga la información del usuario autenticado en el contexto global.
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'select * from users where id = %s', (user_id,)
        )
        g.user = c.fetchone()


# Define una función decoradora que requiere autenticación para acceder a una vista específica
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        """Requiere autenticación para acceder a una vista.

        Args:
            view (función): La vista a proteger con autenticación.

        Returns:
            Si el usuario no está autenticado, redirige a la vista de inicio de sesión ('auth.login').
            Si el usuario está autenticado, permite el acceso a la vista protegida.
        """
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    
    return wrapped_view

# Define una ruta '/logout' bajo el Blueprint 'auth_bp'
@auth_bp.route('/logout')
def logout():
    """
    Cierra la sesion del usuario y redirige a la vista de inicio de sesion.
    """
    session.clear()
    return redirect(url_for('auth.login'))

# Define una ruta '/edit_profile' bajo el Blueprint 'auth_bp' con métodos GET y POST, requiere autenticación
@auth_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        # Obtener datos del formulario
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"Received data: username={username}, password={password}")

        # Validar y actualizar datos del usuario
        if username and password:
            # Realizar la actualización en la base de datos
            db, c = get_db()
            c.execute(
                'UPDATE users SET username = %s, password = %s WHERE id = %s',
                (username, generate_password_hash(password), g.user['id'])
            )
            db.commit()

            flash('User data updated successfully', 'success')
            return redirect(url_for('auth.edit_profile'))

        flash('Invalid data. Both username and password are required', 'error')

    return render_template('auth/edit_profile.html')
