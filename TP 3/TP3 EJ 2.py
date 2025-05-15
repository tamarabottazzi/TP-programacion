# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:55:03 2025

@author: tamar
"""

# Preparar un algoritmo para ingresar dos números naturales N1 y N2, 
# hallar el producto N1 * N2 mediante sumas sucesivas y mostrar el resultado.

# Variable a ingresar: 
N1 = int(input('Ingrese un número natural: '))
N2 = int(input('Ingrese otro número natural: '))


# Se inicializan la variable suma :
suma = 0 # puedo incializar con N1, pero luego en range iré hasta N2

# N1*N2 por suma iterativa es N1+N1+...+N1 N2 veces
for i in range(1, N2+1): #range va de 1 a N2
    suma = suma+ N1
    h = i
# Mostrar resultado N1*N2 vía suma: 
print(f" El producto {N1}*{N2} da", suma)