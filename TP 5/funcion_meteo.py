# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:00:38 2025

@author: tamar
"""

# Realizar una función que permita ingresar las mediciones de temperatura 
# máxima y mínima de 30 días de un mes, validando el ingreso de los días. 
# La función debe retornar el promedio de temperatura del mes, el día de 
# temperatura máxima y el día de temperatura mínima.



def meteo(a,b): #toma una lista a
    #validar lista ingresada: 
    for i in range(len(a)):
        if (a[i]<b[i]):
            a[i] = float(input(f"Ingrese valor correcto de máxima para día {i+1}: "))
            b[i] = float(input(f"Ingrese valor correcto de mínima para día {i+1}: "))
    
    # promedio:
    suma = 0
    for i in range(len(a)):
        suma += a[i]
        if (a[i]==max(a)):    # día de máxima:
            maximo = i+1
        
        if (b[i]==min(b)):    # día de máxima:
            minimo = i+1
         
    promedio = round(suma/len(a),3)
    return [a, b, promedio, maximo, minimo]
    
    



   
        
    
