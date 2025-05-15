# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:35:14 2025

@author: tamar
"""

# Escribir un algoritmo que nos indique si hace frío o calor en función de una
# temperatura y los parámetros de frío/calor ingresados por el usuario.


t = int(input('Ingrese la temperatura actual: '))

#sensa = input('Ingrese su sensación térmica predominante (frío o calor): ')

if (t>=37):
    print('Sofocante')
elif (t>=30):
    print('Cálido')
elif (t>=20):
    print('Templado')
elif (t>=10):
    print('Fresco a frío')
elif (t>= 5):
    print('Frío')
else:
    print('Helado')

