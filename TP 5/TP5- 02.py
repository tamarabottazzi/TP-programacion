# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:27:38 2025

@author: tamar
"""

# Escribir una función para calcular el factorial de un número. 
# Validar el ingreso del número con otra función diferente.

# Ingrese el usuario un número natural:

n = int(input('Ingrese un número natural: '))

# Función validar número ingresado:
def validar(x):
    # Validar que un nro entero sea natural
    if (x<=0):
        print(x, 'es valor negativo, es incorrecto')
        x =int(input('Ingrese un número natural: '))
    else: 
        print(x,'es válido')
    return validar

# Aplica la validación del número ingresado: 
validar(n)

# Función factorial: 
def fact(y): # Factorial de un nro natural
    prod = 1
    for i in range(y):
        prod = prod*(i+1)
    return prod

# Aplicar factorial a n:
print(fact(n))        
    