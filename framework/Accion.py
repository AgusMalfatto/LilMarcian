import yfinance as yf
import pandas as pd

class Stock:
    """
    Atributos:
        - symbol(string)

    Metodos:
        - get_stock_json() -> dict
    TODO:
    - Eleccion del periodo de tiempo
    - Tiempo de cada vela
    * get_historical_data que se le pueda pasar el periodo a la accion
    """
    
    def __init__(self, symbol="AAPL") -> None:
        self.symbol = symbol

    def get_stock_json(self) -> str:
        """Obtiene datos históricos de precios para una acción y los devuelve en formato JSON.

        Utiliza la función `get_historical_data` para obtener los datos históricos y luego los
        convierte en un formato JSON en forma de cadena.

        Returns:
            str: Los datos históricos de precios en formato JSON como una cadena.
        """
        historical_data = self.get_historical_data()
        # Eliminar las horas, minutos y segundos de la columna de fecha
        stock_data = pd.DataFrame(historical_data)
        historical_data['Date'] = historical_data['Date'].dt.strftime("%Y-%m-%d")
        stock_data_json = stock_data.to_json(orient='records', date_format="iso")
        return stock_data_json
    

    def get_historical_data(self, period="2y") -> pd.DataFrame:
        """Obtiene datos históricos de precios para una acción.

        Args:
            period (str, optional): El período de tiempo para obtener los datos históricos, por defecto "2y" (2 años).

        Returns:
            pandas.DataFrame: Un DataFrame de Pandas con los datos históricos de precios.
        """
        stock = yf.Ticker(self.symbol)
        historical_data = stock.history(period=period)
        historical_data = historical_data.reset_index()
        return historical_data



# Codigo para probar atributos rapidamente
# Esto solo se ejecuta si se corre este archivo
if __name__ == "__main__":
    s = Stock()
    print(type(s.get_historical_data()))
