# -*- coding: utf-8 -*-
"""
Created on Wed May 28 20:37:54 2025

@author: tamar
"""

romano = "MCMXCVIII" 

x = "RATA"
y = "AGRADECIDA"


for caracter in romano:
    print(caracter)
    
def contarA(s):
    contar = 0
    for caracter in s:
        if (caracter=="A"):
            contar += 1
    
    return contar

print(contarA(romano), contarA(x), contarA(y))





