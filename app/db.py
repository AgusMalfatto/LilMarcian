# Importa el conector MySQL, el módulo click y objetos de Flask
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext

# Importa las instrucciones de inicialización de la base de datos desde el módulo 'schema'
from .schema import instructions

# Función para obtener o crear una conexión a la base de datos
def get_db():
    """
    Obtiene o crea una conexion a la base de datos.

    Returns:
        Una tupla que contiene la conexión a la base de datos y su cursor.
    """
    # Verifica si ya existe una conexión en el contexto global de la aplicación (g)
    if 'db' not in g: 
        # Si no existe, crea una nueva conexión y un cursor asociado
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True) # Se utiliza un cursor tipo diccionario
    # Retorna la conexión y el cursor
    return g.db, g.c


# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    """
    Cierra la conexion a la base de datos en el caso que este abierta.
    """
    # Intenta obtener y eliminar la conexión del contexto global (g)
    db = g.pop('db', None)
    
    # Si la conexión existe, ciérrala
    if db is not None:
        db.close()
        

# Función para inicializar la base de datos con las instrucciones en schema.py
def init_db():
    """
    Inicializa la base de datos con las instrucciones en schema.py
    """
    # Obtiene la conexión y el cursor utilizando la función get_db
    db, c = get_db()

    # Ejecuta cada instrucción de inicialización almacenada en el módulo 'schema'
    for i in instructions:
        c.execute(i)

    # Confirma los cambios en la base de datos
    db.commit()


# Comando 'init-db' para inicializar la base de datos desde la línea de comandos
@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Comando para inicializar la base de datos en la aplicacion
    """
    # Ejecuta la función init_db al ser llamado desde la línea de comandos
    init_db()
    # Imprime un mensaje indicando que la base de datos ha sido inicializada
    click.echo('Base de datos inicializada')


# Función para inicializar la aplicación con funciones de cierre de la base de datos y 
# comandos de inicialización"""
def init_app(app):
    """
    Inicializa la aplicación con funciones de cierre de base de datos y comandos de
    inicializacion de base de datos.
    """
    # Indica que la función close_db debe ejecutarse al cerrar el contexto de la aplicación
    app.teardown_appcontext(close_db)
    
    # Indica que la función close_db debe ejecutarse al cerrar el contexto de la aplicación
    app.cli.add_command(init_db_command)




