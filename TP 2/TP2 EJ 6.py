# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:22:56 2025

@author: tamar
"""

#Ingresar un número n y verificar si es múltiplo de 3 o 5.

x = -15

resto3 = x%3 
resto5 = x%5

if ((resto3 == 0) and (resto5 == 0)):
    print(x, 'es múltiplo de 3 y de 5')
elif (resto5 ==0):
    print(x, 'es múltiplo de 5')
elif (resto3 ==0):
    print(x, 'es múltiplo de 3')
else: 
    print('No es múltiplo ni de 3 ni de 5')
 