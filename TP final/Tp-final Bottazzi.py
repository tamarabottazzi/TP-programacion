# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 11:58:12 2025

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
import euler 
import euler_mejorado
import runge_kutta
import math

# Ingresar datos de la ecuación diferencial (PVI):    

# Valores iniciales(x0,y0) =
x0 = 0
y0 = 2

# Definir la EDO: dy/dx = 2x+y
def modelo(x, y):
    
    return 2* x+y

# Ingresar datos del paso y del x final:
x1 = 1
h = 0.1 # tiene que ser paso para que llegue en pasos enteros

# Llamar a la función Euler y calcular:    

pares_euler = euler.euler(x0,y0,x1,h)

# Llamar a la función Euler mejorada y calcular:

pares_eulermejorado = euler_mejorado.eulermejorado(x0,y0,x1,h)

# Llamar a la función Runge Kutta y calcular:

pares_rungekutta = runge_kutta.rungekutta(x0,y0,x1,h)

# Solución teórica (si la hubiera):    
    
from sympy import symbols, sympify
from scipy.integrate import solve_ivp


# Condiciones iniciales: y(0) = 1
sol2 = solve_ivp(modelo, [0, 1], [2], t_eval=np.linspace(0, 1, 100))


sol = [4*math.exp(x0+h*i)-2*(x0+h*i)-2 for i in range(int((x1-x0)/h)+1)]
s = np.array(sol)    
#sol_teo = s.reshape(1,int((x1-x0)/h+1))

 
    

import matplotlib.pyplot as plt

# Graficar todas las soluciones obtenidas en un mismo gráfico
    
    
plt.plot(pares_euler[:,0], pares_euler[:,1],'ro', label = 'Euler')
plt.plot(pares_eulermejorado[:,0],pares_eulermejorado[:,1],'g^', label = 'Euler mejorado')
plt.plot(pares_rungekutta[:,0],pares_rungekutta[:,1],'bs', label = 'Runge Kutta K=4')
#plt.plot(pares_euler[:,0], s,'r--', label = 'Sol. Teórica')
plt.plot(sol2.t, sol2.y[0], label = 'Sol. Teórica')
plt.ylabel('y')
plt.xlabel('x')
plt.title("Soluciones numéricas")
#plt.legend('emrt')
plt.legend()
plt.grid(True)       # Muestra la cuadrícula

# Mostrar el gráfico:
plt.show()


# Acá podemos incorporar algún paquete solver de ecuaciones diferenciales 
# (opcional)

# Comparar soluciones con norma y cálculo del error:

from numpy import linalg as LA
# Para calcular la norma del vector error

error_euler = LA.norm(np.array(sol)-np.array(pares_euler[:, 1]))
error_eulermejorado = LA.norm(np.array(sol)-np.array(pares_eulermejorado[:, 1]))
error_rungekutta = LA.norm(np.array(sol)-np.array(pares_rungekutta[:, 1]))

if (error_euler<error_eulermejorado) and (error_euler<error_rungekutta):
    print('El método que mejor aproxima es Euler con error', error_euler)
elif (error_eulermejorado< error_euler) and (error_eulermejorado<error_rungekutta):
    print('El método que mejor aproxima es Euler Mejorado con error', error_eulermejorado)
elif (error_rungekutta<error_euler) and (error_rungekutta<error_eulermejorado):
    print('El método que mejor aproxima es Runge Kutta con error', error_rungekutta)

    
# Armar tabla de datos comparativa con pandas:

import pandas as pd

d = {"x_i": pares_euler[:,0], "Sol. Teórica": sol, "Euler": pares_euler[:,1], "Euler Mejorado": pares_eulermejorado[:,1], "Runge-Kutta": pares_rungekutta[:,1]}

df =pd.DataFrame(d)

print(df)

# Preguntar al usuario si quiere armar tabla de excel con valores:
    
opcion = input('¿Quiere imprimir los datos en una tabla de excel? S/N: ') 
# Nombre del archivo de Excel donde deseas almacenar los datos
nombre_archivo = "datos.xlsx"


if (opcion=="S"):
    df.to_excel(nombre_archivo, index=False)











    