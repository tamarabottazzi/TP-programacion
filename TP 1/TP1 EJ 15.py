# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:18:36 2025

@author: tamar
"""


"""
Consigna--> Calculadora de Descuentos: Crea un programa que solicite al usuario
el precio original de un producto y el porcentaje de descuento que se le 
aplicará. Luego, calcula el precio final después del descuento y muestra el 
resultado.
"""

precio = float(input('Ingrese el precio original del producto: '))

descuento = float(input('Ingrese el procentaje de descuento: '))

precio_final = round(precio- precio* descuento/100, 2)

print('El precio final del producto es de ', precio_final, '$')