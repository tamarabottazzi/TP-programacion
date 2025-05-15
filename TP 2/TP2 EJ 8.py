# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:47:46 2025

@author: tamar
"""

# Ingresar las calificaciones obtenidas en los dos exámenes de Análisis 
# Matemático y, eventualmente si corresponde, las calificaciones del 
# recuperatorio y el integrador e informe la condición final en la cursada 
# y la calificación en caso de promoción. Recuerde que la calificación para 
# promoción es el redondeo del promedio de los exámenes.


parcial1 = int(input('Nota 1er parcial: '))
parcial2 = int(input('Nota 2do parcial: '))

promedio = int((parcial1+parcial2)/2)

if ((parcial1>=7) and (parcial2>=7)):
    print('Promociona con nota igual a ', promedio)
elif ((parcial1>=4) and (parcial2>=4)):
    print('Regulariza la materia')
elif ((parcial1<4) and (parcial1<4)):
    integrador = int(input('Ingrese nota integrador: '))
    if (integrador>=4):
        print('Regulariza la materia')
    else: 
        print('Desaprueba la materia')
else:
    recup = int(input('Ingrese nota recuperatorio: '))
    if (recup>=4):
        print('Regulariza la materia')
    else: 
        print('Desaprueba la materia')
   
# Otra opción:
# IF parcial1 < 4 AND parcial2 < 4 
#     condicion <-- libre
# ELIF parcial1 >=7 AND parcial2 >= 7 
#     condicion <-- promocion
#     promedio <-- (parcial1+parcial2)/2
# ELIF 4<= parcial1 AND 4<=parcial2 AND PROMEDIO < 7
#     condicion <-- regular
# ELIF 4<= parcial1 AND 4<=parcial2 AND PROMEDIO >= 7
#     integ <-- Ingrese nota integrador
#     IF integ >=8
#         condicion <-- promocion
#         PROMEDIO <-- integ
#     ELSE
#         condicion <-- regular
# ELIF parcial1 >=4 AND parcial2 < 4
#     recu <-- Solicitar nota recuperatorio parcial2
#     IF recu >= 4
#         condicion <-- regular
#     ELSE
#         condicion <-- libre
# ELIF parcial1 < 4 AND parcial2 >=4
#     recu <-- Solicitar nota recuperatorio parcial1
#     IF recu >= 4
#         condicion <-- regular
#     ELSE
#         condicion <-- libre
    
# Mostrar condicion
# IF condicion == promocion
#     Mostrar promedio   
# """
    