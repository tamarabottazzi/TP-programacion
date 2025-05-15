# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:29:30 2025

@author: tamar
"""

# Diseñe un algoritmo que lea tres longitudes y determine si forman o no un 
# triángulo. Si es un triángulo determine de qué tipo de triángulo se trata 
# entre: equilátero (si tiene tres lados iguales), isósceles (si tiene dos 
# lados iguales) o escaleno (si tiene tres lados desiguales). Considere que 
# para formar un triángulo se requiere que: "el lado mayor sea menor que la 
# suma de los otros dos lados".



l1 = 3
l2 = 23
l3 = 3

lmax =  max(l1,l2,l3)

if (lmax<l1+l2+l3-lmax):
    if ((l1==l2) and (l2==l3)):
        print('Forman un triángulo equilátero')
    elif ((l1==l2) or (l1==l3)):
        print('Forman un triángulo isósceles')
    elif (l2==l3):
        print('Forman un triángulo isósceles')
    else: 
        print('Forman un triángulo escaleno')
else: 
    print('No forman un tríangulo')