import yfinance as yf
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.layers.recurrent import LSTM
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


"""   PREPARACIÓN DE DATOS   """


# Consulto historial y agrego la media movil de 10
data = yf.download("TSLA", start='2010-09-18', end='2023-09-18')
df = pd.DataFrame(data)
df['SMA_10'] = df['Close'].rolling(window=10).mean()
df.dropna(subset=['SMA_10'], inplace=True)
df.reset_index(inplace=True)



""""   CREACIÓN DE LA RED NEURONAL   """







""" 
# Seleccionar características y etiquetas
features = df[['SMA_10']]
labels = df['SMA_10']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Normalizar características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Reshape de los datos para ser compatibles con LSTM
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)


# Creo la Red Neuronal
model = Sequential()

# Agrego capas recurrentes
model.add(LSTM(units=15, return_sequences=True, input_shape=(X_train.shape[1], 1), activation='tanh'))
model.add(LSTM(units=15, return_sequences=True, input_shape=(X_train.shape[1], 1), activation='relu'))
#model.add(LSTM(units=45, return_sequences=True, input_shape=(X_train.shape[1], 1), activation='elu'))
model.add(Dense(units=1)) # Capa densa para la salida.

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
model.fit(X_train, y_train, epochs=230, batch_size=32)

test_loss = model.evaluate(X_test, y_test)
print(f'Pérdida de datos de prueba: {test_loss}') 


"""   #PREDICCIONES
"""


dfPredict = df[len(df)-10:len(df)]
min_value = df['SMA_10'].min()
max_value = df['SMA_10'].max()

# Aplica la normalización min-max a la columna 'SMA_10'
dfPredict['SMA_10_normalized'] = (dfPredict['SMA_10'] - min_value) / (max_value - min_value)

array_input = np.array(dfPredict['SMA_10_normalized'])
array_input = array_input.reshape(1, 10, 1)
#print(array_input)
predict_values = model.predict(array_input)
print(f"Predicción para valores futuros: {predict_values}") """