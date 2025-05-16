# -*- coding: utf-8 -*-
"""
Created on Fri May 16 11:21:55 2025

@author: tamar
"""

# Escribe una función en Python que tome un número entero n como argumento y 
# calcule una aproximación de π utilizando la serie infinita de Leibniz para 
# π: π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...) hasta el n-ésimo término.

# Ingresar número entero: 
    
n = 1000

# Función Leibniz para pi:
def aproxipi(x):
    sumaparcial = 0
    for i in range(x):
        sumaparcial += (-1)**i/(2*i+1)
        print(sumaparcial) #puse para chequear que está calculando bien los
        # términos de la suma parcial        
    
    return (4*sumaparcial)

# Aplicar función al n ingresado:
y = aproxipi(n)

print(f"La aproximación de orden {n} de pi es {y}")    

        
        
    