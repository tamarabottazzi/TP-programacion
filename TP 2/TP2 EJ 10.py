# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:52:54 2025

@author: tamar
"""

# Diseñe un algoritmo que califique el puntaje obtenido en el 
# lanzamiento de tres dados en función a la cantidad seis obtenidos, 
# de acuerdo a lo siguiente:
#    • Seis en los tres dados, excelente.
#    • Seis en dos dados, muy bien.
#    • Seis en un dado, regular.
#    • Ningún seis, pésimo.


# Lanzamiento de tres dados: 
dado1 = 5
dado2 = 5
dado3 = 1

# Calificación según cantidad de 6 obtenidos:
if (dado1+dado2+dado3==18):
    print('Excelente')
elif ((dado1+dado2==12) or (dado2+dado3==12)):
    print('Muy bueno')
elif (dado1+dado3==12): 
    print('Muy bueno')
elif ((dado1==6) or (dado2==6)):
    print('Regular')
elif (dado3==6):
    print('Regular')
else:
    print('Pésimo')
