# -*- coding: utf-8 -*-
"""
Created on Sun May  4 12:39:58 2025

@author: tamar
"""

# Ingresando un número natural N, construir un algoritmo para hallar y mostrar 
# por pantalla los divisores naturales de N.

# Ingresar número natural:
N = int(input('Ingrese un número natural: '))

# Inicializar lista de divisores:
listadivisores = []

# Encontrar divisores propios: 
for i in range(1,N//2+1):
    if (N%i==0):
        listadivisores.extend([i])

# Agregar N a la lista:
listadivisores.extend([N])

#Mostrar divisores de N:
print(f"Los divisores naturales de {N} son {listadivisores}")
