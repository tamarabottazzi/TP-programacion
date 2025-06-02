# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:39:14 2025

@author: tamar
"""

# Cree una función que tome una lista como entrada y devuelva una nueva lista 
# sin elementos duplicados, manteniendo el orden original.


x = [1, 1, 3, 3, 4, -1, 8, 0, 0, 1, "AB", "BA", "BB", "AB"]

def sindupli(a):
    """  

    Parameters
    ----------
    a : TYPE: lista
        DESCRIPTION. lista de valores cualesquiera

    Returns
    -------
    Nueva lista sin valores repetidos

    """
    lista_completa = a
    
    lista_nueva =[]

    for i in a: # se recorren todos los elementos de la lista a
        if i not in lista_nueva: # si i no está en la lista nueva, se agrega
            lista_nueva.append(i)

    return lista_nueva

y = sindupli(x)
#print(y)


# Se puede hacer con conjuntos pero perdería el orden:
#z = set(x)
#print(z)
   
    
 
print(sindupli(x))
            
    