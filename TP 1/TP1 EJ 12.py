# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 18:51:45 2025

@author: tamar
"""

# Escribir un algoritmo que permita ingresar un valor para X y los 
# coeficientes A, B y C del polinomio: P(X)= AX2 + BX + C; e informe el 
# valor del polinomio.


x = float(input('x: '))
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

pa = a*x*x+b*x+c

print('El valor del polinomio ax^2+bx+c en x=',x, 'es', pa  )