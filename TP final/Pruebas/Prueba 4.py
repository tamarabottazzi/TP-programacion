# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 19:55:56 2025

@author: tamar
"""

# Prueba 2: 
    # 1) datos fijos de entrada: x0 ,y0, xf (los 3 negativos) y h (más chico) 
    # 2) f(x,y) = 1/(x+2), x0 cerca de la región de indeterminación de f
    # 3) 3 métodos
    # 4) Prueba de imprimir la tabla excel


import numpy as np

# Ingresar datos de la ecuación diferencial (PVI):   

# Ingresar valores iniciales(x0,y0) =
x0 = -1.8
y0 = -2

# Ingresar datos del paso y del x final:
xf = -1 # Valor final (mayor a x0)
h = 0.05 # Paso (menor a xf-x0)

# Ingresar métodos a realizar:

# def agregar_strings_a_lista():
#     """
#     Crea una lista pidiendo al usuario que ingrese strings.
#     """
#     num_strings = int(input("¿Cuántos métodos quieres usar? "))
#     mi_lista = []
#     if (num_strings==3):
#         mi_lista = ['euler','euler-mejorado', 'runge-kutta']
#     else: 
#         for i in range(num_strings):
#             string = input(f"Introduce el método número {i+1} euler, euler-mejorado o ""runge-kutta"" : ")
#             mi_lista.append(string)
#     return mi_lista

# metodos = agregar_strings_a_lista()
metodos = ['euler','euler-mejorado', 'runge-kutta']

from sympy import symbols, sympify

# Definir las variables
x, y = symbols('x y')

# Ingresar función como texto:
#entrada = input("Ingresa la función en x y y (por ejemplo: 2*x + y): ")
entrada = 1/(x+2)

# Convertir el texto en expresión simbólica
f = sympify(entrada)

#Pasos totales de los métodos:
pasos_totales = int((xf-x0)/h)+1


# Convertir f a función numérica para usar en el solver:

from sympy.utilities.lambdify import lambdify

f_num = lambdify((x, y), f, 'numpy')

def modelo(x, y):
    
    return f_num(x, y)

# Solución teórica (si la hubiera):    
    
from scipy.integrate import solve_ivp

# Condiciones iniciales: y(0) = 1
sol2 = solve_ivp(modelo, [x0, xf], [y0], t_eval=np.linspace(x0, xf, 100))

# Solución téorica muestreada sólo en los intervalos necesarios:
sol3 = solve_ivp(modelo, [x0, xf], [y0], t_eval=np.linspace(x0, xf, pasos_totales))

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
from numpy import linalg as LA

# Lista con errores: 
    
errores_valor = []
errores_nombre = []

for metodo in metodos:
    if (metodo=='euler'):
        # Llamar a la función Euler y calcular:  
        pares_euler = euler(x0,y0,xf,h)
        plt.plot(pares_euler[:,0], pares_euler[:,1],'ro', label = 'Euler')
        # Calcular error y poner en lista de errores:
        error_euler = LA.norm(s3-np.array(pares_euler[:, 1]))**2
        errores_valor.append([error_euler])
        errores_nombre.append('euler')
       # valores_euler= pares_euler[:,1]
    elif (metodo=='euler-mejorado'):
        # Llamar a la función Euler mejorada y calcular:
        pares_eulermejorado = eulermejorado(x0,y0,xf,h)
        plt.plot(pares_eulermejorado[:,0],pares_eulermejorado[:,1],'g^', label = 'Euler mejorado')
        # Calcular error y poner en lista de errores:
        error_eulermejorado = LA.norm(s3-np.array(pares_eulermejorado[:, 1]))**2
        errores_valor.append([error_eulermejorado])
        errores_nombre.append('euler-mejorado')
    elif (metodo=='runge-kutta'):
        # Llamar a la función Runge Kutta, calcular y graficar:
        pares_rungekutta = rungekutta(x0,y0,xf,h)
        plt.plot(pares_rungekutta[:,0],pares_rungekutta[:,1],'bs', label = 'Runge Kutta K=4')
        # Calcular error y poner en lista de errores:
        error_rungekutta = LA.norm(s3-np.array(pares_rungekutta[:, 1]))**2
        errores_valor.append([error_rungekutta])
        errores_nombre.append('runge-kutta')

           
# Graficar todas las soluciones obtenidas en un mismo gráfico
        
plt.plot(sol2.t, sol2.y[0], label = 'Sol. Teórica')
plt.ylabel('y')
plt.xlabel('x')
plt.title("Soluciones numéricas")
plt.legend()
plt.grid(True)       # Muestra la cuadrícula

# Mostrar el gráfico:
plt.show()

# Comparar soluciones con norma y cálculo del error:
    
minimo = min(errores_valor)

for i in range(len(errores_valor)):
    if (errores_valor[i]== minimo):
        print(f"El método que mejor aproxima es {errores_nombre[i]} con error ", minimo)

    
# Armar tabla de datos comparativa con pandas:

import pandas as pd

# Armo dicccionario con los métodos usados y valores hallados:

valores_x = np.zeros(pasos_totales)
for i in range(1,pasos_totales):
    valores_x[i] += x0+ h*i 
    

clave = ["x_i", "Sol. Teórica"]
valores = [valores_x, s3 ]
for i in range(len(metodos)):
    clave.extend([metodos[i]])
    if (metodos[i]=='euler'):
        valores.extend([pares_euler[:,1]])
    elif (metodos[i]=='euler-mejorado'):
        valores.extend([pares_eulermejorado[:,1]])
    elif (metodos[i]=='runge-kutta'):
        valores.extend([pares_rungekutta[:,1]])
        
d = {}
for i in range(len(clave)):
    d[clave[i]] = valores[i]


df =pd.DataFrame(d)

print(df)

# Preguntar al usuario si quiere armar tabla de excel con valores:
    
opcion = input('¿Quiere imprimir los datos en una tabla de excel? S/N: ') 
# Nombre del archivo de Excel donde deseas almacenar los datos
nombre_archivo = "datos.xlsx"


if (opcion=="S"):
    df.to_excel(nombre_archivo, index=False)
    
 