# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 10:30:53 2025

@author: tamar
"""

import numpy as np

#import euler


# x0 = 0
# y0 = 2
# x1 = 1

# h = 0.1 # tiene que ser paso para que llegue en pasos enteros



def func(x,y): #ingresar la función f(x,y)

    f = 2*x+y

    return f


def eulermejorado(x_inicial,y_inicial,x_final,paso):
    """
    Parameters
    ----------
    x_inicial : TYPE float
        DESCRIPTION. (variable independiente) tiempo inicial
    y_inicial : TYPE float
        DESCRIPTION. (variable dependiente) posición inicial de la y incógnita
    x_final : TYPE float
        DESCRIPTION.(variable independiente) tiempo final
    paso : TYPE float
        DESCRIPTION. longitud del paso por iteración

    Returns
    -------
    par (dupla) array (xi,yi) de la solución numérica del PVI 

    """
    total_pasos = int((x_final-x_inicial)/paso)+1
    print(total_pasos)
    par = np.zeros((total_pasos,2))
    
    par[0,0] += x_inicial
    par[0,1] += y_inicial
    f = 0
    
    for i in range(1,total_pasos):
        par[i,0] += x_inicial+ paso*i 
        f = func(par[i,0], func(par[i-1,0],par[i-1,1]))
        par[i,1] += par[i-1,1]+(func(par[i-1,0], par[i-1,1])+f)*paso/2
   
    return par

# pares = eulermejorado(x0,y0,x1,h)

# print(pares)

