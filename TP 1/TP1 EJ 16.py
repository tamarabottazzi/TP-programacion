# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:24:16 2025

@author: tamar
"""

# Cálculo del Área de un Triángulo: Escribe un programa que pida al usuario 
# la base y la altura de un triángulo y calcule su área utilizando la fórmula:
# Área = (base * altura) / 2. Muestra el resultado en pantalla.

base = float(input('base (en cm): '))

altura = float(input('altura (en cm): '))

area = base*altura/2

print ('El área del triángulo es ', area)