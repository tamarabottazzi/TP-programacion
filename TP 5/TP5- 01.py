# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:10:12 2025

@author: tamar
"""

# Retome la calculadora del TP04 y vuelva a programarla a partir de un conjunto
# de funciones propias.

#a = 10
a = float(input('a= ')) 

#b = 2
b = float(input('b= '))

# Operación elegida:
operacion = input('Elija operación S/P/R/D: ')

# Funciones de la calculadora:

def suma(x,y):
    suma = x + y
    return suma

def prod(x,y):
    prod = x * y
    return prod

def resta(x,y):
    resta = x - y
    return resta

def div(x,y):
    division = round(x/y,4)
    return division

# Realizar operación según elección del usuario:
if (operacion=="S"):
    print(f"{a} + {b} es igual a", suma(a,b))
elif (operacion=="P"):
    print(f"{a} * {b} es igual a", prod(a,b))
elif (operacion=="R"):
    print(f"{a} - {b} es igual a", resta(a,b))
else:
    if (b==0): # por si el usuario ingresa un divisor nulo
        print("No se puede dividir por cero") 
        b = float(input('Elija otro b= '))
        print(f"{a} / {b} es igual a", div(a,b))
    else: 
        print(f"{a} / {b} es igual a", div(a,b))
