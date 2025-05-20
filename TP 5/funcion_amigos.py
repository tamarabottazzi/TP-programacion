# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:32:37 2025

@author: tamar
"""

# Escribe una función que tome dos números enteros positivos a y b como 
# argumentos. La función deberá determinar si a y b son números amigos, 
# es decir, la suma de los divisores propios de a es igual a b y viceversa.



def amigos(a,b): #función amigos
    #inicializo suma de divisores propios de a y de b:
    sumadiva = 0
    sumadivb = 0
    # hallar divisores propios de a y b e irlos sumando:
    for i in range(1,a//2+1):
        if (a%(i) ==0):
            #print(i)
            sumadiva += i
    
    for j in range(1,b//2+1):
        if (b%j ==0):
            #print(j)
            sumadivb += j
    
   # ver si son amigos: usamos variable booleana x
    if ((sumadiva==b) and (sumadivb==a)):    
        x = True
    else:
        x = False
    return x

    