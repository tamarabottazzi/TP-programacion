# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:27:38 2025

@author: tamar
"""

# Escribir una función para calcular el factorial de un número. 
# Validar el ingreso del número con otra función diferente.

# Ingrese el usuario un número natural:

n = int(input('Ingrese un número entero no negativo: '))

# Función validar número ingresado:
def validar(x):
    # Validar que un nro entero sea natural
    while (x<0): 
        print(x, 'es valor negativo, es incorrecto')
        x =int(input('Ingrese un número natural: '))
    return x
#print(x,'es válido')    
    
# Aplica la validación del número ingresado: 
nval = validar(n)

# Función factorial: 
def fact(y): # Factorial de un nro natural o 0
    prod = 1
    #m = y
    if (y==0):
        prod = 1       
    else:
        for i in range(y):
            prod = prod*(i+1)  
            
     #   m = m* fact(y-1) (no funciona)

    return prod


# Aplicar factorial a nval:
print(fact(nval))        
    