# Importa functools para funciones de orden superior y elementos necesarios de Flask
import functools
from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for, session, redirect
)

# Crea un Blueprint llamado 'auth' con prefijo de URL '/auth'
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Importa las vistas asociadas al Blueprint desde el módulo actual (views.py)
from . import views
