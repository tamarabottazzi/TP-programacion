# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:08:35 2025

@author: tamar
"""

# Desarrollar un programa que permita ingresar por teclado la cantidad 
# milímetros de lluvia caída en Luján para una semana y calcule el promedio. 
# El programa además deberá alertar al usuario cuando la cantidad de lluvia 
# caída en la semana supere una cantidad ingresada por el usuario, a efectos 
# de poner en marcha acciones preventivas contra las posibles inundaciones.

# Inicializo variable precipitaciones diarias: 
    
mmtotal = 0
ppmax = float(input('Ingrese valor máximo de precipitaciones acumuladas en mm: '))
dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'] 

# Ciclo para ingresar por teclado la cantidad de milímetros de lluvia caída en
# Luján para una semana, día por día y sumar acumulado:
for dia in dias:
    diario = float(input(f"Ingrese mm día {dia}: "))
    mmtotal += diario
    
    if (mmtotal>ppmax): # Alertar al usuario por lluvias excesivas
        print(f"Las precipitaciones acumuladas al día {dia} superan el valor de {ppmax} mm.")
         
# Calcula e informa el promedio:
promedio = round(mmtotal/7,1)
print('El promedio semanal de precipitiaciones fue de ', promedio, 'mm')



        


