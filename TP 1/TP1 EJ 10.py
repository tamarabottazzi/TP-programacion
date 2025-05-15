# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 17:48:13 2025

@author: tamar
"""

# Diseñe un algoritmo para sumar dos marcas de tiempo dadas en días, 
# horas, minutos y segundos.

# Primer tiempo registrado: 
    
x1 = 2132045

dias1= x1//1000000

horas1 = (x1//10000)%100

minutos1 = (x1//100)%100

seg1 = x1%100

# Segundo tiempo registrado:

x2 = 12230559

dias2= x2//1000000

horas2 = (x2//10000)%100

minutos2 = (x1//100)%100

seg2 = x2%100


print(dias1, horas1, minutos1, seg1)

print(dias2, horas2, minutos2, seg2)

dias_total = dias1 + dias2
horas_total = horas1 + horas2
minutos_total = minutos1 + minutos2
seg_total = seg1 + seg2

if (seg_total//60==1):
    minutos_total = minutos_total +1
    seg_total = seg_total-60

if (minutos_total//60==1):
    horas_total = horas_total +1
    minutos_total = minutos_total-60

if (horas_total//24==1):
    dias_total = dias_total +1
    horas_total = horas_total-24


print('El tiempo total entre las dos marcas fue de: ', dias_total, 'días', horas_total, 'horas', minutos_total, 'minutos', seg_total, 'segundos')





 
