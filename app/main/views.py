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
    resultado = {
            'stock': 'AAPL',
            'valor': None
        }
        
    stocks = get_stocks()

    if request.method == 'POST':
        # Obtengo el symbolo de la accion
        stock = request.form['stock']
        resultado['stock'] = stock
        # Creo la prediccion
        prediction = create_prediction(symbol=stock)
        resultado['valor'] = round(prediction['resultado'][0][0], 2)
        return render_template('index.html', resultado=resultado, stocks=stocks)

    return render_template('index.html', resultado=resultado, stocks=stocks)        




@main_bp.route('/acciones', methods=['GET'])
def get_stocks():
    db, c = get_db()
    c.execute('SELECT symbol, name FROM stocks')
    stocks = c.fetchall()
    
    return stocks

