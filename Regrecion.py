# -*- coding: utf-8 -*-
"""
Created on Sat May 7 00:13:12 2023

@author: LoboM
"""

"""Aqui utilizamos la biblioteca scikit-learn para realizar una regresión lineal múltiple"""

"""importamos todas las librerias"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

"""Se crean tres arrays NumPy: x1, x2 y y, que representan los datos de entrada y la variable 
objetivo. En este caso, x1 y x2 son variables predictoras, y y es la variable objetivo"""

x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([2, 4, 6, 8, 10])
y = np.array([5, 10, 15, 20, 25])

df = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})

modelo = LinearRegression().fit(df[['x1', 'x2']], df['y'])

print('Coeficientes: ', modelo.coef_)

"""Se crean nuevos valores de entrada en un DataFrame llamado nuevos_valores. En este caso, 
se define un nuevo conjunto de datos con un valor de x1 igual a 6 y un valor de x2 igual a 12"""

nuevos_valores = pd.DataFrame({'x1': [6], 'x2': [12]})
prediccion = modelo.predict(nuevos_valores)
print('Predicción: ', prediccion)

"""Se imprime la predicción resultante, que muestra el valor estimado de la variable objetivo
 (y) para los nuevos valores de entrada proporcionados"""