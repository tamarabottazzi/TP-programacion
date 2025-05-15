# -*- coding: utf-8 -*-
"""
Created on Sun May  4 12:02:20 2025

@author: tamar
"""

# Construir un algoritmo para ingresar un número natural n, y que calcule y 
# muestre por pantalla el factorial de n.


# Ingresar n natural:
n = int(input('Ingrese un número natural: '))

# Inicializar productoria:
producto = 1

for i in range(1,n+1):
    producto *=i
    
print(f"el factorial de {n} es: ", producto)
    

