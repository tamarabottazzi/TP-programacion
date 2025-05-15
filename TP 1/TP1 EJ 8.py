# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:45:39 2025

@author: tamar
"""

# Escribir un algoritmo que determine la suma de las cifras de un 
# número entero positivo de 4 cifras.


n = int(input('Ingrese número de 4 cifras positivo:'))

#int trunca a la parte entera por abajo

m = int(n/1000)

c = int((n-m*1000)/100)

d = int((n-m*1000-c*100)/10)

u = int((n-m*1000-c*100-d*10))

suma = m+c+d+u

print('La suma de sus dígitos es: ', suma)


