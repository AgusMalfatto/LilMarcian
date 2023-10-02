import yfinance as yf
import pandas as pd

# Retorna el historial de la acción recibida
def get_stock(symbol = "AAPL"):
    # Crear una instancia de la acción
    stock = yf.Ticker(symbol)

    # Obtener el historial de precios de la acción
    historical_data = stock.history(period="2y")

    # Reiniciar el índice para convertir la fecha en una columna
    historical_data = historical_data.reset_index()

    stock_data = pd.DataFrame(historical_data)

    # Eliminar las horas, minutos y segundos de la columna de fecha
    historical_data['Date'] = historical_data['Date'].dt.strftime("%Y-%m-%d")
    
    stock_data_json = stock_data.to_json(orient='records', date_format="iso")

    return stock_data_json