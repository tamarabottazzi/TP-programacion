# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:03:07 2025

@author: tamar
"""

# Cree un script que, sabiendo cuántos pesos argentinos tiene una persona 
#ahorrada en su cuenta (almacenando ese monto en una variable), muestre 
#en pantalla los montos convertidos en dólares 
#(U$1 = $1330.5), reales ($R1 = $182.76), y euros (€1 = $1176.38). 
#La salida del programa debe tener el siguiente formato:
# Usted tiene $XXX pesos argentinos, los cuales se convierten en:
#- U$XXX dólares.
#- R$XXX reales.
#- €XXX euros.

# TESTING: para las pruebas acerca de si funciona bien el código hay
# que probar con valores que sabemos que es lo que van a dar:
# x = 1350.5
# y = 182.76
# z = 1176.38    
    
# en x se almacena el valor de los ahorros
# si no pide que ingrese el usuario no usar input

x = float(input('Ingrese su saldo en pesos: '))

# round se usa para redondear a los decimales que quieras, 
# en este caso a 2
dolar = 1350.5
real = 182.76
euro = 1176.38

d = round(x/dolar, 2)
r = round(x/ real, 2)
e = round(x/ euro, 2)


#Mostrar los resultados del ti
print('Usted tiene $', x, 'pesos argentinos, los cuales se convierten\  en: ')
print('U$', d, 'dólares' )
print('R$', r, 'reales' )
print('€', e, 'euros' )