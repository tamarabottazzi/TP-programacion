# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:37:21 2025

@author: tamar
"""

#     18. A lo largo del curso vamos a programar una pequeña calculadora. 
# Por ahora, implemente las 4 operaciones básicas de una calculadora para 
# hacer cálculos entre dos números que serán ingresados por un usuario:
#    • Un programa que sume dos números,
#    • Un programa que multiplique dos números,
#    • Un programa que realice la resta entre dos números,
#    • Un programa que realice la división entre dos números.

#a = 10
a = float(input('a= ')) 

#b = 2
b = float(input('b= '))


suma = a+b
mult = a*b 
resta = a-b
div = round(a/b,4)

print(a, '+', b, '=', suma)
print(a, '*', b, '=', mult)
print(a, '-', b, '=', resta)
print(a, '/', b, '=', div)