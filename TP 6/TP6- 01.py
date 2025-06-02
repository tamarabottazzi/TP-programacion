# -*- coding: utf-8 -*-
"""
Created on Thu May 29 16:08:30 2025

@author: tamar
"""

# Defina una función que tome una cadena de texto como entrada y devuelva un 
# diccionario que cuente la frecuencia de cada carácter en la cadena.


x = "hola mundo, como están?"

def freqcharacter(a):
    """
    
    Parameters
    ----------
    a : TYPE string
        DESCRIPTION. cadena de texto

    Returns
    -------
    diccionario con Frencuencia de cada caracter en la cadena

    """
    # armo lista con caracteres no repetidos:    
    no_repetidos = []
    for i in a:
        if i not in no_repetidos:
            no_repetidos.append(i)
            
    # armar lista de frecuencias:
    frecuencia = []
    for j in no_repetidos:
        contar = 0
        for l in a:
            if (l==j):
                contar += 1
        
        frecuencia.append(contar)
    
    # armar pares caracteres-frecuencia:
    pares = []
    for l in range(len(no_repetidos)):
        pares.append((no_repetidos[l], frecuencia[l]))
    
    # armar diccionario: 
    frecuencia_caracteres = dict(pares)
    
    return frecuencia_caracteres


d = freqcharacter(x)

print(d)
            
        
        
    
    
    