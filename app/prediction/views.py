from datetime import datetime
from flask import (
    flash, g, redirect, render_template, request, url_for, jsonify
)
from . import prediction_bp
from werkzeug.exceptions import abort
from app.auth.views import login_required
from app.db import get_db
import json

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

@prediction_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_prediction(symbol="AAPL"):
    # La acción se debe capturar del HTML seleccionado por el usuario
    modelFit, model = getModel(symbol)
    predictionValue = prediction(symbol, model)
    resultado = {'resultado': predictionValue}

        # Obtener el precio actual utilizando yfinance
    stock_data = yf.Ticker(symbol)
    current_price = stock_data.history(period='1d')['Close'].iloc[-1]

    # Definir las variables datetime, precio_actual y precio_prediccion
    now = datetime.now()
    date_created = now.strftime('%Y-%m-%d %H:%M:%S')
    date_prediction = date_created  # Puedes cambiar esto según la lógica de tu aplicación
    precio_actual = current_price

    # Asegúrate de que predictionValue tiene la estructura esperada antes de intentar acceder a sus elementos.
    print(predictionValue)  # Agrega esta línea para ver el contenido de predictionValue
    precio_prediccion = predictionValue[0][0]
    # Después de obtener la predicción, guárdala en la base de datos
    db, c = get_db()
    c.execute(
        'INSERT INTO his_predictions (id_user, symbol, date_created, date_prediction, price_created, price_prediction) VALUES (%s, %s, %s, %s, %s, %s)',
        (g.user['id'], symbol, date_created, date_prediction, precio_actual, precio_prediccion)
    )
    db.commit()
    return resultado


def getModel(stock, begin='2023-10-01'):
    # Consulto los datos de la acción
    data = yf.download(stock, start=begin)
    df = pd.DataFrame(data)
    df.reset_index(inplace=True)

    # Defino dos decimales para los datos flotantes
    pd.options.display.float_format = '{:.2f}'.format

    """ Extraer datos """

    # Extraigo los datos de cierre de la acciones para los datos de entrada (data_in) y salida (data_out).
    data_in = df[['Close']]
    data_out = df[['Close']]

    # Los datos de entrada serán los cierres de la acciones desde el primer dato hasta el anteúltimo.
    data_in_subset = data_in.iloc[:len(data_in)-1]
    # Los datos de salida serán los cierres de las acciones desde el segundo hasta el último.
    data_out_subset = data_out.iloc[1:]
    # Con esto logro que el primer dato (data_in[0]) sea la entrada del segundo dato (data_out[1])

    """ Preparación de datos """

    # Realizamos el split de X e Y en los sets de entrenamiento (train) y test
    X_train, X_test, y_train, y_test = train_test_split(data_in_subset, data_out_subset, test_size=0.20, random_state=1992)

    """ Creación del modelo """

    # Creación del modelo de regreción lineal
    model = LinearRegression(fit_intercept=True)
    # Entrenamientod el modelo
    model.fit(X_train, y_train)

    # Realizamos la predicción con los X_test
    y_pred = model.predict(X_test)

    """ Cálculo de errores """

    # Calculamos el Error Cuadrático Medio
    mse = mean_squared_error(y_test, y_pred)

    # Calculamos el Coeficiente de Determinación
    r2 = r2_score(y_test, y_pred)

    """ Mejora del dataframe para visualización de resultados """

    # Crear un DataFrame con los últimos 40 valores reales
    cant_dataTest = len(y_pred)
    df_test = df.iloc[-cant_dataTest:][['Date', 'Close']].copy()

    # Crear un DataFrame para las predicciones
    prediction = pd.DataFrame(y_pred, columns=['Predictions'])

    # Asignar las predicciones al DataFrame df_test
    df_test['Prediction'] = prediction['Predictions'].values

    # Reiniciar el índice si es necesario
    df_test.reset_index(drop=True, inplace=True)

    # Calculo la diferencia entre los datos de cierre y predicciones
    df_test['Diference'] = df_test['Close'] - df_test['Prediction']

    df_test['Porcentaje'] = df_test['Diference'] * 100 / df_test['Close']
    df_test['Porcentaje'] = df_test['Porcentaje'].apply(lambda x: -x if x < 0 else x)

    dict_from_df = df_test.to_dict(orient='list')
    dict_from_df['MSE'] = mse
    dict_from_df['R2'] = r2
    return (dict_from_df, model)


def prediction(stock, model):
    # Obtener los datos de hoy (o hasta el último día disponible)
    today = pd.to_datetime('today').strftime('%Y-%m-%d')

    datos_hasta_hoy = yf.download(stock, start='2023-09-01', end=today)
    datos_hasta_hoy.reset_index(inplace=True)

    # Extraer el último dato de cierre
    close_today = datos_hasta_hoy['Close'].iloc[-1]

    # Crear un DataFrame para hacer la predicción de mañana
    data = pd.DataFrame({'Close': [close_today]})

    # Hacer la predicción para mañana
    prediction_tomorrow = model.predict(data) # Retorna un numpyArray

    return prediction_tomorrow