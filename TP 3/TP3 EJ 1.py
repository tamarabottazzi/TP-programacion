# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 20:59:16 2025

@author: tamar
"""

# Calcular la suma y el producto de los números pares comprendidos entre 
# 20 y 500.

# Valores cotas:
m = 20
n= 500
 

# Se inicializan las variables suma y producto:
suma = 0
producto = 1


# Notar que range(m, n) incluye x pero excluye y por eso va n+1
# 2 es el paso
# por default range comienza en 0

for i in range(m, n+1, 2):
    suma += i
    # suma = suma + i
    producto *= i 
    # producto = producto*i
    
print('La suma da ', suma)
print('El producto da ', producto)