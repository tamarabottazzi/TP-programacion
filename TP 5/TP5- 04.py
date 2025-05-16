# -*- coding: utf-8 -*-
"""
Created on Fri May 16 11:41:24 2025

@author: tamar
"""

# Crea una función generadora que produzca una secuencia de números primos, 
# iniciando por el primero y devolviendo el próximo cada vez que el usuario 
# ingrese “próximo”. La función deberá terminar cuando en vez de presionar 
# siguiente, indique “terminar”.


# preguntar si próximo o siguiente primo

# si es próximo, buscar el proximo primo y preguntar de nuevo

# si no terminar ahí



pregunta = input('próximo o terminar (P/T): ')

def proxprimo(preg):
    x= 2
    while (preg=="P"):
      y = "no primo"       
      while (y == "no primo"): 
           p = x//2 # Posibles divisores inicializando en x/2
           while ((x%(p)>0) and (p<=x/2)): #mientras p no sea divisor 
               p -=1

           if (p==1):
               print(x)               
               y = "primo"
              # preg = input('próximo o terminar: ')
               x +=1
           else: 
               x +=1
               y = "no primo"
      preg = input('próximo o terminar (P/T): ')
             
    return x
        
proxprimo(pregunta)        
