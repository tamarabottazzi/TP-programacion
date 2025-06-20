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

# Función euler mejorado: 
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
    #print(total_pasos)
    par = np.zeros((total_pasos,2))
    
    par[0,0] += x_inicial
    par[0,1] += y_inicial
    
    for i in range(1,total_pasos):
        par[i,0] += x_inicial+ paso*i 
        f_anterior = f.subs({x: par[i-1,0], y: par[i-1,1]}) # f evaluada en paso anterior
        y_euler = par[i-1,1]+paso*(f_anterior)#euler para yi actual
        f_actual = f.subs({x: par[i,0], y: y_euler})
        par[i,1] += par[i-1,1]+(f_anterior+f_actual)*paso/2
    
    return par

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time:.10f} segundos")


