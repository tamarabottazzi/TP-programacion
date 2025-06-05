# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:07:33 2025

@author: tamar
"""

import numpy as np

# x0 = 0
# y0 = 2
# x1 = 1

# h = 0.1 # tiene que ser paso para que llegue en pasos enteros



def func(x,y): #ingresar la función f(x,y)

    f = 2*x+y

    return f


def rungekutta(x_inicial,y_inicial,x_final,paso):
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
    par_xy = np.zeros((total_pasos,2))
    
    par_xy[0,0] += x_inicial
    par_xy[0,1] += y_inicial
    
    for i in range(1,total_pasos):
        par_xy[i,0] += x_inicial+ paso*i 
        k1 = func(par_xy[i-1,0], par_xy[i-1,1])
        k2 = func(par_xy[i-1,0]+paso/2, par_xy[i-1,1]+k1*paso/2)
        k3 = func(par_xy[i-1,0]+paso/2, par_xy[i-1,1]+k2*paso/2)
        k4 = func(par_xy[i-1,0]+paso, par_xy[i-1,1]+k3*paso)        
        par_xy[i,1] += par_xy[i-1,1]+(k1+k2+k3+k4)*paso/6
        
    return par_xy

# pares = rungekutta(x0,y0,x1,h)

# print(pares)

