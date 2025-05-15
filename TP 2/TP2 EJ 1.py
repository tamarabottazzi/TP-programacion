# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:37:21 2025

@author: tamar
"""

# La calculadora del TP01 tenía varios problemas:
# a. En primer lugar, ¿Qué sucede cuando queremos dividir por 0? ¿Qué debería suceder?
# Incorpore esta funcionalidad al script.
# b. Otro de los problemas que tiene nuestra calculadora es que debo llamar un programa 
# distinto para cada operación básica. Genere un script que utilice el código anterior, 
# en el cual, en un único script el usuario pueda elegir cual de las 4 operaciones va a realizar (suma, resta, multiplicación, división).

#a = 10
a = float(input('a= ')) 

#b = 2
b = float(input('b= '))

# Operación elegida:
operacion = input('Ingrese nombre de operación a realizar: ')

if (operacion == "suma"): 
    suma = a+b
    print(a, '+', b, '=', suma)
elif (operacion == "producto"):
    mult = a*b 
    print(a, '*', b, '=', mult)
elif (operacion == "resta"):
    resta = a-b
    print(a, '-', b, '=', resta)
elif (operacion == "división"):
    if (b == 0):
        print('El divisor no puede ser cero')
        b= float(input(' Ingrese otro b= '))
    div = round(a/b,4)
    print(a, '/', b, '=', div)
else: 
    print('No se entiende la operación a realizar')

input()