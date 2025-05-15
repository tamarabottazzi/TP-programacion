# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 20:29:27 2025

@author: tamar
"""

# Ingrese las calificaciones de un parcial para un grupo de N (definido por el 
# usuario) alumnos del curso Programación y calcule el promedio de 
# calificaciones y porcentaje de aprobados, desaprobados y ausentes 
# (los ausentes se representarán con el valor 99 como calificación)."

# Ingresar Número de estudiantes:
n =int(input('Ingrese el número total de estudiantes: '))

# Ingresar las calificaciones de un parcial de todos los estudiantes en una lista:
x = [int(input('Ingrese la nota del estudiante: ')) for i in range(n)]

# Inicializo las variables suma de notas, aprobados, desaprobados y ausentes:
suma = 0
aprobados = 0
desaprobados = 0
ausentes = 0

# Clasificar notas y ausentes:
for i in range(n):
   if (x[i]<4):
       desaprobados +=1
       suma += x[i]
   elif (x[i]<11):
       aprobados +=1
       suma += x[i]
   else:
       ausentes +=1

       
if (ausentes== n): # Si todos estuvieron ausentes:
    print('No hubo presentes en el examen')
else: # Promedio, orcentajes de aprobados, desap y ausentes sobre el total::
    promedio = round(suma/(aprobados+desaprobados), 2)
    porc_ap = round(aprobados*100/n,2)
    porc_des = round(desaprobados*100/n,2)
    porc_aus = round(ausentes*100/n,2)
    print('El promedio de los exámenes es de ', promedio)
    print('El porcentaje de aprobados es de ', porc_ap, '%')
    print('El porcentaje de desaprobados es de ', porc_des, '%')
    print('El porcentaje de ausentes es de ', porc_aus, '%')

        
            

        
    
    

    
    