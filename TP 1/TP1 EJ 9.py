# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 16:05:35 2025

@author: tamar
"""

# Escribir un algoritmo que permita ingresar la longitud de un lado 
# de un triángulo equilátero y muestre su perímetro y su área.

# Tengo que llamar a este módulo math para la raíz cuadrada
#from math import sqrt

lado = float(input('Ingrese la longitud de un lado del triángulo equilátero en cm: '))

per = 3* lado 

#Dos formas distintas: con módulo math.sqrt y usando el exponente fraccionarioa)

#area = round(sqrt(3)*(lado**2)/4, 3)
area = round(3**(0.5)*(lado**2)/4, 3)

print('Perímetro: ', per, 'cm')
print('Área: ', area, 'cm2')