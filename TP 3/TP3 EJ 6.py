# -*- coding: utf-8 -*-
"""
Created on Thu May  1 19:26:34 2025

@author: tamar
"""

# Los números perfectos son números naturales que son iguales a la suma de 
# todos sus divisores propios excepto él mismo. Así, por ejemplo, el 6 es un
# número perfecto ya que es igual a la suma de sus tres divisores propios: 
# 1, 2 y 3. Se pide escribir un programa que calcule los cuatro primeros 
# números perfectos.

    
contar = 0
n = 6
suma = 0

while (contar<4) : # ciclo while para seguir hasta que obtengamos los primeros 4 nros perfectos:
#for n in range(1,30000):
    for i in range(1,(n//2)+1): #ver si n es perfecto
        if (n%i==0):
            suma +=i #sumar los divisores propios
    
    if (suma== n):
        contar +=1 #contar si es n perfecto
        print(n, 'es perfecto')
        suma = 0 # resetear suma
    else:
        suma = 0 # resetear suma
    #    print(n, 'no es perfecto')
    n = n+1 #iterar cada entero hasta que se cumpla la condición
        

