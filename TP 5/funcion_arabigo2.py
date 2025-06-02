# -*- coding: utf-8 -*-
"""
Created on Wed May 28 19:47:26 2025

@author: tamar
"""

romano1 = "MDXCIX"
romano2 = "MCMXCVIII"
romano3 = "MCDXLIV"

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
    
    resta = 0
    
    x= romano
    
    for i in range(len(romano)):
        if (x[i]== "M"): 
            # que me sume 1000 por cada M
            miles += 1000
        elif (x[i]== "D"):
            # sume 500 por cada D
            centenas += 500            
        elif (x[i]== "C"):
            # sume 100 por cada C
            centenas += 100
        elif (x[i]== "L"):
            # sume 50 por cada L
            decenas += 50
        elif (x[i]== "X"):
            # sume 10 por cada X
            decenas += 10
        elif (x[i]== "V"):
            # sume 5 por cada V
            unidades += 5
        elif (x[i]== "I"):
            # sume 1 por cada I
            unidades += 1 
        
    # restar 100, 10 0 1 de más:
    for i in range(len(romano)-1):
        if (x[i]=="C") and (x[i+1]=="M"):
            # restar 200 porque sumé 100 de más en el loop anterior
            resta -=200
        elif (x[i]=="C") and (x[i+1]=="D"):
            resta -= 200
        
        if (x[i]=="X") and (x[i+1]=="C"):
            # restar 20 porque sumé 10 de más en el loop anterior
            resta -=20
        elif (x[i]=="X") and (x[i+1]=="L"):
            resta -= 20
        
        if (x[i]=="I") and (x[i+1]=="X"):
            # restar 2 porque sume 1 de más en el loop anterior
            resta -=2
        elif (x[i]=="I") and (x[i+1]=="V"):
            resta -= 2
    
    arabe = miles+ centenas+ decenas+ unidades+ resta
   # print(miles, centenas, decenas, unidades, resta)
    
         
    return arabe

print(arabigo(romano1))
print(arabigo(romano2))
print(arabigo(romano3))

        
