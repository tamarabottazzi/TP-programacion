# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:25:01 2025

@author: tamar
"""

# Defina funciones que tomen dos conjuntos como entrada y devuelvan la unión y 
#la diferencia simétrica entre ellos.


x = {2, 4, 6, 8, 10}

y = {1, 3, 5, 7, 9}


def union(a,b):
    """
    

    Parameters
    ----------
    a : TYPE: set
        DESCRIPTION.conjunto de valores a
    b : TYPE: set
        DESCRIPTION. conjunto de valores b

    Returns
    -------
    Operacion unión entre a yb

    """
    uni = a.union(b)
    
    return uni

def inter(a,b):
    """
    

    Parameters
    ----------
    a : TYPE: set
        DESCRIPTION.conjunto de valores a
    b : TYPE: set
        DESCRIPTION. conjunto de valores b

    Returns
    -------
    Operacion intersección entre a yb

    """
    
    interseccion = a.intersection(b)
    
    return interseccion

def dif(a,b):
    """
    

    Parameters
    ----------
    a : TYPE: set
        DESCRIPTION.conjunto de valores a
    b : TYPE: set
        DESCRIPTION. conjunto de valores b

    Returns
    -------
    Operacion diferencia simétrica entre a yb

    """
    
    diferencia = a.difference(b)
    
    return diferencia

print(union(x,y))
print(inter(x,y))
print(dif(x,y))