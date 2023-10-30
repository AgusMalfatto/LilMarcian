import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions
from .config import config

def get_db():
    if 'db' not in g: 
        g.db = mysql.connector.connect(
            host = config['DATABASE_HOST'],
            user = config['DATABASE_USER'],
            password = config['DATABASE_PASSWORD'],
            database = config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()
        

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)




