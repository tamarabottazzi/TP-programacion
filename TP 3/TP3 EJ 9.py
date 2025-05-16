# -*- coding: utf-8 -*-
"""
Created on Sun May  4 11:35:45 2025

@author: tamar
"""

# Escribe un programa que verifique si un número dado es primo o no. 
# Un número primo es aquel que solo es divisible por 1 y por sí mismo.

# Ingresar n:

n = int(input('Ingrese un número entero: '))

# Posibles divisores inicializando en n/2: 
p = n//2

while ((n%(p)>0) and (p<=n/2)): #mientras p no sea divisor 
    p -=1

if (p==1):
    print(n, ' es primo')
else: 
    print(n,' no es primo')
        
    