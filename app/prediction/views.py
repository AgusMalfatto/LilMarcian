from flask import (
    flash, g, redirect, render_template, request, url_for, jsonify
)
from . import prediction_bp
from werkzeug.exceptions import abort
from app.auth.views import login_required
from app.db import get_db
import json

@prediction_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_prediction():
    resultado = {'resultado': 'Esto es una prueba.'}
    return resultado
