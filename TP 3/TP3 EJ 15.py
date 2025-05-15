# -*- coding: utf-8 -*-
"""
Created on Sun May  4 17:43:59 2025

@author: tamar
"""

# Una empresa liquida sus salarios de la siguiente manera: Básico + 5%
# del básico por año de antigüedad + $15 por hijo – 10% del básico por 
# retenciones. Ingresar el sueldo básico (único para todos los empleados) y el 
# apellido de cada empleado, emitiendo luego cada uno de los recibos 
# correspondientes. Validar la antigüedad entre 1 y 25 y la cantidad de hijos 
# 
# entre 0 y 10. Considerar como valor de corte apellido = “FIN”. Finalmente, 
#mostrar: 
#    • Totales generales por concepto (básico, antigüedad, salario familiar y 
# retenciones).
#    • Nombre del empleado que obtuvo la mayor retribución (neto).

# Ingresar el sueldo básico (único para todos los empleados):
basico = 1000

# Inicializar listas: 

apellido = [input('Ingrese apellido del empleado: ')]
antiguedad = [int(input('Antigüedad en años: '))]
hijos = [int(input('Hijos: '))]
bruto = [basico+basico*0.05*antiguedad[0]+hijos[0]*15]
neto = [bruto[0]-basico*0.1]
n= 0

#Ingresar datos de cada empleado:
while (apellido[n]!= "FIN"):   #itera hasta la palabra FIN 
    apellido.extend([input('Ingrese apellido del empleado: ')]) #apellido   
    antiguedad.extend([int(input('Antigüedad en años: '))])  #Antiguedad
    hijos.extend([int(input('Hijos: '))]) # Cantidad de hijos:
    bruto.extend([basico+basico*0.05*antiguedad[n]+hijos[n]*15]) # sueldo bruto
    neto.extend([bruto[n]-basico*0.1]) # sueldo neto
    n += 1

# Mostrar cada uno de los recibos:
for i in range(0,n): 
    print('Empleado: ', apellido[i])
    print('Básico:', basico, '$')
    print('Antigüedad: ',basico*0.05*antiguedad[i], '$' )
    print('Salario familiar: ', hijos[i]*15, '$')
    print('Retenciones: ', basico*0.10, '$')
    print('Sueldo bruto: ', bruto[i], '$' )
    print('Sueldo neto: ', neto[i], '$')


