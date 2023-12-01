# Importa la clase Blueprint de Flask
from flask import Blueprint

# Crea un Blueprint llamado 'main' sin prefijo de URL específico
main_bp = Blueprint('main', __name__)

# Importa las vistas asociadas al Blueprint desde el módulo actual (presumiblemente views.py)
from . import views