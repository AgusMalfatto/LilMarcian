from . import auth_bp

import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for, session, redirect
)

from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select id from users where username = %s', (username,)
        ) 
        if not username:
            error = 'Username es requerido'
        if not password:
            error = 'Password es requerido'
        elif c.fetchone() is not None:
            error = f'Usuario {username} se encuentra registrado'
        print(generate_password_hash(password))
        if error is None:
            c.execute(
                'insert into users (username, email, password ) values (%s, %s, %s)',
                (username, email, generate_password_hash(password))
            )
            db.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
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
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'select * from users where id = %s', (user_id,)
        )
        g.user = c.fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    
    return wrapped_view
    
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

