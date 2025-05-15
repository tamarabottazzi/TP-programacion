# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:21:45 2025

@author: tamar
"""

# En una carrera de turismo carretera el tiempo se mide en minutos, 
# segundos y centésimas de segundo y el espacio recorrido se mide en 
# metros. Dados estos datos, escribir un algoritmo para calcular la 
# velocidad promedio de un automóvil en km/h.

d = float(input ('distancia recorrida:' ))/1000

m = int(input('minutos:' ))
s = float(input ('segundos y centésimos (en formato ss.cc): '))

tts = m * 60+ s

disthora = round(3600 * d/tts,2)

print('Velocidad:', disthora, 'km/h' )  



