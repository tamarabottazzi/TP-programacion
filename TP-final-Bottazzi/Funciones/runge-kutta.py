# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 17:46:46 2025

@author: tamar
"""

import numpy as np

from sympy import symbols, sympify

import time

start_time = time.time()


# Definir las variables
x, y = symbols('x y')

# Ingresar función como texto:
#entrada = input("Ingresa la función en x y y (por ejemplo: 2*x + y): ")
entrada = x*y+y

# Convertir el texto en expresión simbólica
f = sympify(entrada)

# Función Runge-Kutta:
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
    #print(total_pasos)
    par_xy = np.zeros((total_pasos,2))
    
    par_xy[0,0] += x_inicial
    par_xy[0,1] += y_inicial
    
    for i in range(1,total_pasos):
        par_xy[i,0] += x_inicial+ paso*i 
        k1 = f.subs({x: par_xy[i-1,0], y: par_xy[i-1,1]})
        k2 = f.subs({x: par_xy[i-1,0]+paso/2, y: par_xy[i-1,1]+k1*paso/2})
        k3 = f.subs({x: par_xy[i-1,0]+paso/2, y: par_xy[i-1,1]+k2*paso/2})
        k4 = f.subs({x: par_xy[i-1,0]+paso, y: par_xy[i-1,1]+k3*paso})        
        par_xy[i,1] += par_xy[i-1,1]+(k1+2*k2+2*k3+k4)*paso/6
        
    return par_xy

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time:.10f} segundos")
