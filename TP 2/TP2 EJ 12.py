# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 18:58:14 2025

@author: tamar
"""

# Calculadora de IMC (Índice de Masa Corporal): Implementa un programa 
# en Python que calcule el índice de masa corporal (IMC) de una persona. 
# El programa debe solicitar el peso (en kilogramos) y la altura (en metros) 
# al usuario, calcular el IMC utilizando la fórmula: 
# IMC = peso / (altura ** 2), y luego mostrar el resultado en pantalla.

# Modifique el ejercicio 13 del TP01 para indicar al usuario la 
# clasificación de su IMC. Indague en internet respecto a los rangos de 
# cada categoría.


peso = float(input('Peso (en kg): '))
altura = float(input ('Altura (en mts): ')) 
imc = round(peso/(altura**2),1)

print('Su IMC es de ', imc)


if (imc>40):
    print('Categoría según OMS: Obesidad Mórbida')
elif (imc>=35):
    print('Categoría según OMS: Obesidad grado II')
elif (imc>=30):
    print('Categoría según OMS: Obesidad grado I')
elif (imc>=25):
    print('Categoría según OMS: Sobrepeso')
elif (imc>=18):
    print('Categoría según OMS: Aceptable')
else: 
    print('Categoría según OMS: Bajo peso')


    