# -*- coding: utf-8 -*-
"""
Created on Fri May  2 15:28:42 2025

@author: tamar
"""

# Escribir un programa que imprima la secuencia de todas las combinaciones de 
# hora y minuto de un día, comenzando por 01:00 y terminando por 12:59.

#n= 1

#x =list()

for n in range(25): #horas del día
    for i in range(60): # Minutos en una hora
        if (i<10):
            print(f"{n}:{0}{i}")
        else:
            print(f"{n}:{i}")
        
    
