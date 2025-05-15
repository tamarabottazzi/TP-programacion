# -*- coding: utf-8 -*-
"""
Created on Sun May  4 12:50:34 2025

@author: tamar
"""

# Ingresar una secuencia de calificaciones numéricas, entre 0 y 10, que 
# finaliza con el valor de corte = –1. Validar el ingreso, calcular e imprimir 
# el promedio de calificaciones del curso, el número y porcentaje de aprobados
# y el número y porcentaje de desaprobados.

# Inicializo coordenadas de la lista para usar while:
i=0
suma_notas = 0 
contar_notas = 0 #cantidad de examenes rendidos
aprobados = 0
desaprobados = 0
lista_notas =[int(input('Ingrese nota del examen: '))]

# Ingresar notas en una lista hasta que se que corte con -1:
while(lista_notas[i]>-1): #corta el usuario con -1
    lista_notas.extend([int(input('Ingrese nota del examen: '))]) 
    suma_notas += lista_notas[i]
    contar_notas += 1
    if (lista_notas[i]>=4):
        aprobados += 1
    else: 
        desaprobados +=1
    
    i += 1
    

# Cacular y mostar promedio:
promedio = round(suma_notas/contar_notas, 2)
print('El promedio del curso es de ', promedio)

# Calcular y mostar cantidad de aprobados y desaprobados y porcentajes:  
porc_aprobados = round(aprobados*100/contar_notas,2)
porc_desaprobados = round(desaprobados*100/contar_notas,2)
print(f"Hay {aprobados} aprobados, que corresponden al {porc_aprobados} % del total")
print(f"Hay {desaprobados} desaprobados, que corresponden al {porc_desaprobados} % del total")
    
    

    
    
    