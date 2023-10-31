import mysql.connector

import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

def get_db():
    """
    Obtiene o crea una conexion a la base de datos.

    Returns:
        Una tupla que contiene la conexión a la base de datos y su cursor.
    """
    if 'db' not in g: 
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    """
    Cierra la conexion a la base de datos en el caso que este abierta.
    """
    db = g.pop('db', None)
    
    if db is not None:
        db.close()
        

def init_db():
    """
    Inicializa la base de datos con las instrucciones en schema.py
    """
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Comando para inicializar la base de datos en la aplicacion
    """
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):
    """
    Inicializa la aplicación con funciones de cierre de base de datos y comandos de
    inicializacion de base de datos.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)




