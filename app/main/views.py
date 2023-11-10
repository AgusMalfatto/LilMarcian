from flask import (
    flash, g, redirect, render_template, request, url_for
)
from . import main_bp
from werkzeug.exceptions import abort
from app.auth.views import login_required
from app.db import get_db
from app.prediction.views import create_prediction

@main_bp.route('/', methods=['POST', 'GET'])
@login_required
def index():
    resultado = None
    if request.method == 'POST':
        # Obtengo el symbolo de la accion
        stock = request.form['stock']
        # Creo la prediccion
        resultado = create_prediction(symbol=stock)
    stocks = obtener_acciones()
    return render_template('index.html', resultado=resultado, stocks=stocks)



@main_bp.route('/acciones', methods=['GET'])
def obtener_acciones():
    stocks = [
        {'symbol': 'AAPL', 'name': 'Apple Inc.'},
        {'symbol': 'GOOGL', 'name': 'Alphabet Inc.'},
    ]
    return stocks

