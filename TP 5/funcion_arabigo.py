# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:04:13 2025

@author: tamar
"""

# Escribir una función que convierta un número romano a arábigo.
# M = 1000
# D = 500
# C = 100
# L = 50
# X = 10
# V = 5
# I = 1


romano1 = ["M","D","X","C","I","X" ]
romano2 = ["M","C","M","X","C","V","I","I","I" ]
romano3 = ["M","C","D","X","L","I","V" ]

# NO FUNCIONA BIEN, LA VERSIÓN 2 ES LA QUE VA

def arabigo(romano):
    """    

    Parameters
    ----------
    romano : TYPE lista (string)
        DESCRIPTION. números romanos ordenados de mayor

    Returns 
    -------
    Número arábico correspondiente

    """
    miles = 0
    centenas = 0
    decenas = 0
    unidades = 0
    
    x= romano
    
    for i in range(len(romano)):
        if (x[i]== "M") and (x[i-1]!="C"): # que me sume 1000 por cada M y 900 por cada CM
            miles += 1000
        elif (x[i]== "M") and (x[i-1]=="C"):
            miles += 900
            
        if (x[i]== "D") and (x[i-1]!="C"): # que me sume 500 por cada D y 400 por cada CD
            centenas += 500
        elif (x[i]== "D") and (x[i-1]=="C"):
            centenas += 400
                    
        if (x[i]== "C") and (x[i-1]!="X") and (x[i+1]!="M") and (x[i+1]!="D"): 
            # que me sume 100 por cada C y 90 por cada XC
            # que no sea un 100 que resta a 1000
            # que no sea un 100 que resta a 500
            centenas += 100
        elif (x[i]== "C") and (x[i-1]=="X"):
            centenas += 90
            
        if (x[i]== "L") and (x[i-1]!="X"): # que me sume 50 por cada L y 40 por cada XL
            decenas += 50
        elif (x[i]== "L") and (x[i-1]=="X"):
            decenas += 40
            
        if (x[i]== "X") and (x[i-1]!="I") and (x[i+1]!="C") and (x[i+1]!="L"):
            # que me sume 10 por cada X y 9 por cada IX
            # y que no sea un 10 que resta a centenas o cincuentas
            decenas += 10
        elif (x[i]== "X") and (x[i-1]=="I"):
            unidades += 9
            
        if (x[i]== "V") and (x[i-1]!="I"): 
            # que me sume 5 por cada V y 4 por cada IV
            unidades += 5
        elif (x[i]== "V") and (x[i-1]=="I"):
            unidades += 4
            
        if (x[i]== "I"): 
            # que me sume 1 por cada I
            # que no sea un 1 que resta a 5
            unidades += 1
         
    arabe = miles+ centenas+ decenas+ unidades
    print(miles, centenas, decenas, unidades)
    
         
    return arabe

print(arabigo(romano1))
#print(arabigo(romano2))
#print(arabigo(romano3))

            
            
            
            
            
            
            