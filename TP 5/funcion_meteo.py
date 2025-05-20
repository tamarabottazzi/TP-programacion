# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:00:38 2025

@author: tamar
"""

# Realizar una función que permita ingresar las mediciones de temperatura 
# máxima y mínima de 30 días de un mes, validando el ingreso de los días. 
# La función debe retornar el promedio de temperatura del mes, el día de 
# temperatura máxima y el día de temperatura mínima.



def meteo(a): #toma una lista a
    # promedio:
    suma = 0
    for i in range(len(a)):
        suma += a[i]
    
    promedio = round(suma/len(a),3)
    # día de máxima:
    maximo = max(x)
    # día de mínima:
    minimo = min(x)
    
        
    
