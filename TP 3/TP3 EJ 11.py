# -*- coding: utf-8 -*-
"""
Created on Sun May  4 12:06:52 2025

@author: tamar
"""

# Construir un algoritmo para ingresar por el teclado dos números naturales 
# M y N. Hallar el cociente M/N por restas sucesivas y mostrar por pantalla el 
# dividendo, divisor, cociente y resto.

# Ingresar dos nros naturales: 
M = int(input('Ingrese un número entero: '))
N = int(input('Ingrese un número entero: '))


# Compararlos para fijar divisor y dividendo: 
if (N<M): 
   divisor = N
   dividendo = M
else:
   divisor = M
   dividendo = N
   
# Inicializar resto y cociente:
resto = divisor
cociente = 1

# Hacer división por restas sucesivas hasta que el resto sea menor que el 
# divisor:
while (resto>= divisor):
    cociente += 1
    resto = dividendo-cociente*divisor

#Mostrar resultados:
print(f"La división de {dividendo} por {divisor} tiene como cociente {cociente} y resto {resto}")    
    
    