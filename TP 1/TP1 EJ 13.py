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


peso = float(input('Peso (en kg): '))
altura = float(input ('Altura (en mts): ')) 
imc = round(peso/(altura**2),2)

print('Su IMC es de ', imc)