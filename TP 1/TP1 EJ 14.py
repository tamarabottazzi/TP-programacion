# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:13:25 2025

@author: tamar
"""

#    14. Conversión de Temperaturas: Escribe un programa que permita al 
# usuario ingresar una temperatura en grados Celsius y lo convierta a 
# Fahrenheit y Kelvin. Utiliza las siguientes fórmulas:
#    • Fahrenheit = (Celsius * 9/5) + 32
#    • Kelvin = Celsius + 273.15


celsius = float(input('Ingrese temperatura en grados Celsius: '))

faren = (celsius* 9/5)+32
kelvin = celsius + 273.15

print(celsius, 'Grados Celsius son', faren, 'Farenheit y ', kelvin, 'Kelvin') 