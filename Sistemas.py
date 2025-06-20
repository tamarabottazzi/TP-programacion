# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 18:52:58 2025

@author: tamar
"""

import numpy as np

import random

# Matrix diagonal del sistema:

[a11, a12 , a21, a22] = [1, 0, 0, -2]

vector = np.array([1, 0, 0, 2])
matriz = vector.reshape(2,2)

# Paso fijo:
h= 0.1


# Condiciones iniciales random:
a = -10
b = 10
c = -5
d = 25



def rungekutta(x_inicial,y_inicial,x_final,paso, a):
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
    a : autovalor
 
    Returns
    -------
    par (dupla) array (xi,yi) de la solución numérica del PVI y'=ay

    """
    total_pasos = int((x_final-x_inicial)/paso)+1
#    print(total_pasos)
    par_xy = np.zeros((total_pasos,2))
    
    par_xy[0,0] += x_inicial
    par_xy[0,1] += y_inicial
    
    for i in range(1,total_pasos):
        par_xy[i,0] += x_inicial+ paso*i 
        k1 = a* par_xy[i-1,1]
        k2 = a*(par_xy[i-1,1]+k1*paso/2)
        k3 = a* (par_xy[i-1,1]+k2*paso/2)
        k4 = a*(par_xy[i-1,1]+k3*paso)        
        par_xy[i,1] += par_xy[i-1,1]+(k1+2*k2+2*k3+k4)*paso/6
        
    return par_xy

import matplotlib.pyplot as plt

for i in range(30):
    x0 = random.randint(a, b)
    y0 = random.randint(c, d)
    sol1 = rungekutta(x0, y0, x0+10, h, a11)
    sol2 = rungekutta(x0, y0, x0+10, h, a22)
    sol = random.randint(-100, 100)*sol1[:, 1]+random.randint(-100, 100)*sol2[:, 1]
    # plt.plot(sol1[:,0], sol1[:, 1])
    # plt.plot(sol2[:,0], sol2[:, 1])
    plt.plot(sol1[:,0], sol)


# Mostrar el gráfico:
plt.show()
    
