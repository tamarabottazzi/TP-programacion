# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 18:33:54 2025

@author: tamar
"""

# Se solicita un préstamo por S pesos durante M meses a una tasa de interés 
# mensual I. Al final de los M meses la cantidad adeudada es
# = S * (1 + I) ^ M. Escribir un algoritmo al cual se le den los valores 
# de S, M e I, e informe la suma adeudada.

s = 1200000
#s = int(input('Ingrese monto del préstamo: '))

#m =int(input('Ingrese cantidad de meses a financiar: '))
m = 34

I = 0.02

deuda = round(s*(1+I)**m,2)

print('La suma adeudada es de', deuda, 'pesos')