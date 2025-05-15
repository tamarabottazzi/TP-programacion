# -*- coding: utf-8 -*-
"""
Created on Fri May  2 15:52:01 2025

@author: tamar
"""

# ¿Cuál es la suma de los números pares comprendidos entre 300 y 1232?

n1 = 300
n2 = 1232
suma = 0
x = [] 

for i in range(n1, n2+2 ,2):
    suma += i
    x.extend([i])
    
print('La suma de los números pares comprendidos entre 300 y 1232 es ', suma)
    
    