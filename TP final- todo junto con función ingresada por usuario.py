# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 19:55:56 2025

@author: tamar
"""

# Trabajo final:
    
# Crear una función que permita obtener la solución numérica de una ecuación 
# diferencial de 1er orden usando el método de Euler:
    
# Mejorar el método aplicando Euler Mejorado y Runge Kutta de orden 4

# Comparar gráfica y analíticamente las soluciones obtenidas y otras dadas 
# por paquetes o la solución exacta en el caso de que se tenga

# Entrega con archivos de prueba


import numpy as np
#import math

# Ingresar datos de la ecuación diferencial (PVI):    

# Ingresar valores iniciales(x0,y0) =
x0 = 0
y0 = 1
#x0 = float(input('Ingrese valor inicial x0:))
#y0 = float(input('Ingrese valor inicial y0:))

# Ingresar datos del paso y del x final:
x1 = 1
h = 0.1 # tiene que ser paso para que llegue en pasos enteros
#x1 = float(input('Ingrese valor final x1:))
#h = float(input('Ingrese el paso h:))

from sympy import symbols, sympify

# Definir las variables
x, y = symbols('x y')

# Ingresar función como texto
#entrada = input("Ingresa la función en x y y (por ejemplo: 2*x + y): ")
entrada = x*y+y
# Convertir el texto en expresión simbólica
f = sympify(entrada)



# Definir la función de la EDO: dy/dx = 2x+y
# Esto es sólo para comparar las aproximaciones con la sol teórica
# (si la hubiere)

def modelo(x, y):
    
    return x*y+y


# Solución teórica (si la hubiera):    
    
from scipy.integrate import solve_ivp


# Condiciones iniciales: y(0) = 1
sol2 = solve_ivp(modelo, [x0, x1], [y0], t_eval=np.linspace(x0, x1, 100))

# Solución téorica muestreada sólo en los intervalos necesarios:
pasos_totales = int((x1-x0)/h)+1
sol3 = solve_ivp(modelo, [x0, x1], [y0], t_eval=np.linspace(x0, x1, pasos_totales))

s3 = np.array(sol3.y[0])

   
    
# Función euler: 
def euler(x_inicial,y_inicial,x_final,paso):
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
        par_xy[i,1] += par_xy[i-1,1]+f.subs({x: par_xy[i-1,0], y: par_xy[i-1,1]})*paso
    return par_xy

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
        y_euler = par[i-1,1]+paso*(f.subs({x: par[i,0], y: f_anterior}))#euler para yi actual
        f_actual = f.subs({x: par[i,0], y: y_euler})
        par[i,1] += par[i-1,1]+(f_anterior+f_actual)*paso/2
    
    return par


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

import matplotlib.pyplot as plt


# Llamar a la función Euler y calcular:  
pares_euler = euler(x0,y0,x1,h)
# Llamar a la función Euler mejorada y calcular:
pares_eulermejorado = eulermejorado(x0,y0,x1,h)
# Llamar a la función Runge Kutta y calcular:
pares_rungekutta = rungekutta(x0,y0,x1,h)

# Graficar todas las soluciones obtenidas en un mismo gráfico
        
plt.plot(pares_euler[:,0], pares_euler[:,1],'ro', label = 'Euler')
plt.plot(pares_eulermejorado[:,0],pares_eulermejorado[:,1],'g^', label = 'Euler mejorado')
plt.plot(pares_rungekutta[:,0],pares_rungekutta[:,1],'bs', label = 'Runge Kutta K=4')
#plt.plot(pares_euler[:,0], s,'r--', label = 'Sol. Teórica')
plt.plot(sol2.t, sol2.y[0], label = 'Sol. Teórica')
plt.ylabel('y')
plt.xlabel('x')
plt.title("Soluciones numéricas")
plt.legend()
plt.grid(True)       # Muestra la cuadrícula

# Mostrar el gráfico:
plt.show()



# Comparar soluciones con norma y cálculo del error:

from numpy import linalg as LA
# Para calcular la norma al cuadrado del vector error: 

error_euler = LA.norm(s3-np.array(pares_euler[:, 1]))**2
error_eulermejorado = LA.norm(s3-np.array(pares_eulermejorado[:, 1]))**2
error_rungekutta = LA.norm(s3-np.array(pares_rungekutta[:, 1]))**2

if (error_euler<error_eulermejorado) and (error_euler<error_rungekutta):
    print('El método que mejor aproxima es Euler con error', error_euler)
elif (error_eulermejorado< error_euler) and (error_eulermejorado<error_rungekutta):
    print('El método que mejor aproxima es Euler Mejorado con error', error_eulermejorado)
elif (error_rungekutta<error_euler) and (error_rungekutta<error_eulermejorado):
    print('El método que mejor aproxima es Runge Kutta con error', error_rungekutta)

    
# Armar tabla de datos comparativa con pandas:

import pandas as pd

d = {"x_i": pares_euler[:,0], "Sol. Teórica": s3, "Euler": pares_euler[:,1], "Euler Mejorado": pares_eulermejorado[:,1], "Runge-Kutta": pares_rungekutta[:,1]}

df =pd.DataFrame(d)

print(df)

# # Preguntar al usuario si quiere armar tabla de excel con valores:
    
# opcion = input('¿Quiere imprimir los datos en una tabla de excel? S/N: ') 
# # Nombre del archivo de Excel donde deseas almacenar los datos
# nombre_archivo = "datos.xlsx"


# if (opcion=="S"):
#     df.to_excel(nombre_archivo, index=False)
    
 