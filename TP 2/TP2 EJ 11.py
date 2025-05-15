# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 19:15:53 2025

@author: tamar
"""

# Escribir un programa que permita determinar si un punto se encuentra en el 
# interior de un rectángulo, o en alguno de los lados o en el exterior, 
# teniendo como datos dos vértices opuestos de dicho rectángulo.

# Rectángulo de vértices ABCD con A y C opuestos que son dato:

# Vértice A= (a1,a2)
a1 = 0
a2 = 6

# Vértice C=(c1,c2)
c1 = 5
c2 = 0

# Ingresar X=(x1,x2)
x1 = 5
x2 = 10

# Cotas de los intervalos:
a = min(a1,c1)
b = max(a1,c1)

c = min(a2,c2)
d = max(a2,c2)

# Condición para estar en el interior del rectángulo:
    # a<x1<b
    # c<x2<d
if ((a<x1<b) and (c<x2<d)):
    print('el punto está en el interior del rectángulo ABCD')
elif ((x1== a) and (c<x2<d)):
    print('el punto está en uno de los lados del rectángulo ABCD')  
elif ((x1== b) and (c<x2<d)):
    print('el punto está en uno de los lados del rectángulo ABCD')  
elif ((a<x1<b) and (x2== c)):
    print('el punto está en uno de los lados del rectángulo ABCD') 
elif ((a<x1<b) and (x2== d)):
    print('el punto está en uno de los lados del rectángulo ABCD') 
else: 
    print('el punto está en el exterior del rectángulo ABCD')

# vert1_x =-2 
# vert1_y = -2
# vert2_x = -6
# vert2_y = -4

# vert_max_x = max(vert1_x, vert2_x)
# vert_min_x = min(vert1_x, vert2_x)
# vert_max_y = max(vert1_y, vert2_y)
# vert_min_y = min(vert1_y, vert2_y)

# punto_x = 3
# punto_y = 1.5

# # Caso punto interior
# if (vert_min_x < punto_x < vert_max_x) and (vert_min_y <punto_y < vert_max_y):
#     print("Punto interior")
# # Caso punto exterior
# elif (vert_min_x > punto_x or punto_x > vert_max_x) or \
#     (vert_min_y > punto_y or punto_y > vert_max_y):
#     print("Punto exterior")
# else:
#     print("Punto frontera")