# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:02:14 2025

@author: tamar
"""

# Realizar una función que permita ingresar una serie de edades hasta que 
# reciba el valor 999 e indique la cantidad de edades ingresadas que hayan 
# sido mayores que la ingresada en primer lugar.



def edades(y):
    edad1 = y 
    contar = 0
    while (y != 999):
        if (y> edad1):
            contar += 1
        
        y = int(input('Ingrese edad: '))
        
    return contar
        

    
        