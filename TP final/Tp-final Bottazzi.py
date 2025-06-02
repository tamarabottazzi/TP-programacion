# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 11:58:12 2025

@author: tamar
"""

# Idea para el Trabajo final:
    
# Crear una función que permita obtener la solución numérica de una ecuación 
# diferencial de 1er orden usando el método de Euler:
    
# Mejorar el método aplicando Euler Mejorado y Runge Kutta de orden 4

# Comparar gráfica y analíticamente las soluciones obtenidas y otras dadas 
# por paquetes o la solución exacta en el caso de que se tenga


import numpy as np
import euler 
import euler_mejorado
import math

# Ingresar datos de la ecuación diferencial (PVI):    

# Valores iniciales(x0,y0) =
x0 = 0
y0 = 2

# f(x,y) =  me falta mejorarlo para que se pueda ingresar acá


# Ingresar datos del paso y del x final:
x1 = 1
h = 0.1 # tiene que ser paso para que llegue en pasos enteros

# Llamar a la función Euler y calcular:    

pares_euler = euler.euler(x0,y0,x1,h)
pares_eulermejorado = euler_mejorado.eulermejorado(x0,y0,x1,h)


 
# Llamar a la función Euler mejorada y calcular:
    
# Llamar a la función Runge Kutta y calcular:

import matplotlib.pyplot as plt

# Graficar todas las soluciones obtenidas en un mismo gráfico

# Euler: 
    
# Solución teórica (si la hubiera):    
    
# y= 4e^x-2x-2
sol = [4*math.exp(x0+h*i)-2*(x0+h*i)-2 for i in range(int((x1-x0)/h)+1)]
s = np.array(sol)    
#sol_teo = s.reshape(1,int((x1-x0)/h+1))
    
# plt.plot(pares[:1],pares[1:2],'ro', pares[:1], sol_teo, 'bs' )
# plt.ylabel('y')
# plt.xlabel('x')
# plt.show()

plt.plot(pares_euler[:,0],pares_euler[:,1],'ro')
plt.plot(pares_eulermejorado[:,0],pares_eulermejorado[:,1],'g^')
plt.plot(pares_euler[:,0], s, 'bs' )
plt.ylabel('y')
plt.xlabel('x')
plt.title("Soluciones numéricas")
plt.legend('emt')
plt.show()




# Acá podemos incorporar algún paquete solver de ecuaciones diferenciales 
# (opcional)

# Comparar soluciones con norma y cálculo del error:

#error = sol_teo-pares[1:2]
    
    
# Armar tabla de datos comparativa con pandas?

#totales = np.array(list([pares[:,0]]),list([pares[:,0]]),sol)











    