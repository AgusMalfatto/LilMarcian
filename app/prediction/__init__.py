from flask import Blueprint

# Creacion de blueprint
prediction_bp = Blueprint('prediction', __name__, url_prefix='/prediction')

from . import views

