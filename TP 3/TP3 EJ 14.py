# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:53:54 2025

@author: tamar
"""

#     14. Ingresar por teclado una tabla de 600 valores comprendidos entre 
# –45 y 90, se pide:
    # • Encontrar la media de los valores ingresados.
    # • Mostrar en qué posición ingresó el mayor número por última vez.
    # • Mostrar en qué posición ingresó el menor número por última vez.
    # • Mostrar la cantidad de ceros, negativos y positivos ingresados.
    # • Mostrar la cantidad de números inválidos ingresados.
    
    
import random

# Inicializar lista de valores y demás variables de contar: 
n = 600
x = [] # lista original de tamaño n
y = [] # lista sin inválidos de tamaño n menos los inválidos
suma = 0
nulos = 0
positivos = 0
negativos = 0 
invalidos = 0

# Ingresar 600 valores random entre -45 y 90 (en lugar de por teclado):
for i in range(n):
    x.extend([random.randint(-35, 100)]) #valor aleatorio entero en el intervalo (-45,90)

# Inválidos: 
for i in range(n):
    if ((x[i]<-45) or (x[i]>90)):
        invalidos += 1
    else: 
        suma += x[i] # sumar sólo los válidos para la media
        y.extend([x[i]]) # armar lista de válidos

print(f"Hay {invalidos} valores inválidos")
# Media: calcular y mostrar
media = round(suma/n,2)
print('La media es de ', media)


# Máx, mín, ceros, pos, neg e inválidos
minimo = min(y) # mínimo válido
maximo = max(y) # máximo válido
for i in range(n):
    if (x[i]== minimo): # última ubicación del mínimo válido en la lista original
        i0 = i
    
    if (x[i]== maximo): # última ubicación del máximo válido en la lista original
        j0 = i

for i in range(n-invalidos):
    if (y[i]< 0): #contar negativos, positivos y ceros válidos
        negativos += 1
    elif (y[i]>0):
        positivos += 1
    else:
        nulos += 1
      
print(f"El valor mínimo es {minimo} y se aparece por última vez en la posición {i0}")
print(f"El valor máximo es {maximo} y se aparece por última vez en la posición {j0}")
print(f"Hay {nulos} ceros, {negativos} negativos y {positivos} positivos")

        
    


    
    