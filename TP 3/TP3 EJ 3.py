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

# Ciclo para ingresar por teclado la cantidad de milímetros de lluvia caída en
# Luján para una semana, día por día y sumar acumulado:
for i in range(1,8):
    diario = int(input(f"Ingrese mm día {i}: "))
    mmtotal = mmtotal + diario
    
# Calcula e informa el promedio:
promedio = round(mmtotal/7,1)
print('El promedio semanal de precipitiaciones fue de ', promedio, 'mm')

# Alertar al usuario cuando la cantidad de lluvia caída en la semana supere 
# una cantidad preingresada de 60 mm:
if (mmtotal>60):
    print('Alerta por excesivas precipitaciones.')
    print('El total semanal fue de ', mmtotal, 'mm')


        


