# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:38:53 2025

@author: tamar
"""

# Se efectúa una encuesta entre 120 consumidores de cigarrillos. 
# Las respuestas están codificadas como 1, 2 ó 3 según sea la marca elegida. 
# Preparar un algoritmo para ingresar las 120 respuestas, y muestre por 
# pantalla el número de la marca preferida.

# Encuesta en una lista: inicializo la lista con el valor de la encuesta 1

x = [int(input('Ingrese el valor de la 1ra encuesta: '))]

# Inicializo el conteo de cada marca:
marca1 = 0
marca2 = 0
marca3 = 0

if (x[0]==1):
    marca1 += 1
elif (x[0]==2):
    marca2 += 1
else: 
    marca3 = 0


# Ingresar las 119 respuestas restantes ordenadas en la lista x e ir contando
# el acumulado de cada marca:
for i in range(11):
    x.extend([int(input(f"Ingrese encuesta {i+2}:  "))])
    if (x[i+1]==1):
        marca1 += 1
    elif (x[i+1]==2):
        marca2 += 1
    else: 
        marca3 += 1 
 
print(marca1,marca2,marca3)       
 
# Mostrar por pantalla el número de la marca preferida:
if (marca1>marca2):
    if (marca1>marca3):
        print('La marca 1 es la preferida')
    elif (marca1<marca3):
        print('La marca 3 es la preferida')
    else: 
        print('Las marcas 1 y 3 son las preferidas')
elif (marca3>marca2):
    print('La marca 3 es la preferida')
elif (marca2>marca3):
    if (marca2== marca1):
        print('Las marcas 1 y 2 son la preferias')
    else: 
        print('La marca 2 es la preferida')
elif (marca1<marca2):
    print('Las marca 2 y 3 son las preferidas')
else: 
    print('Las tres marcas son elegidas por igual')

        

        
             




                   
        
        


