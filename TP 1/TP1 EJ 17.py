# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:27:45 2025

@author: tamar
"""

# Conversión de Tiempo: Crea un programa que permita al usuario ingresar 
# una cantidad de minutos y lo convierta a horas y minutos. Por ejemplo, 
# si el usuario ingresa 150 minutos, el programa debería mostrar 
# "2 horas y 30 minutos".


t_min = int(input('Ingrese tiempo total en minutos: '))
#t_min = 1215


hs = t_min//60

minutos = t_min%60

print('Son ', hs, 'horas y ', minutos, ' minutos')