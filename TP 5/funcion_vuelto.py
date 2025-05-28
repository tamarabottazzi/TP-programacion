# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:16:01 2025

@author: tamar
"""

# Escribir una función que ingresando el precio de un artículo y la cantidad 
# de dinero con el que paga el cliente, retorne el vuelto utilizando la menor 
# cantidad de billetes posibles 
# (se cuenta con billetes de 50, 20, 10, 5, 2 y 1).



def vuelto(precio, dinero):
    """

    Parameters
    ----------
    precio : integer
        DESCRIPTION. Costo del producto
    dinero : integer
        DESCRIPTION. Dinero que paga el cliente

    Returns
    -------
    list
        lista de cantidad de billetes de 50,20,10,5,2,1 en ese orden que hay
        que dar de vuelto

    """
    vuelto = dinero-precio 
    print(vuelto)
    vuelto_restante = dinero-precio
    contar_50 = 0
    contar_20 = 0
    contar_10 = 0
    contar_5 = 0
    contar_2 = 0
    contar_1 = 0
    
    if (vuelto//50!= 0):
        contar_50 = vuelto//50
        vuelto_restante = vuelto-50* contar_50
        if (vuelto_restante//20!= 0):
            contar_20 = vuelto_restante//20
            vuelto_restante = vuelto_restante-20*contar_20
            print(vuelto_restante)
            if (vuelto_restante//10!= 0):
                contar_10 = vuelto_restante//10
                vuelto_restante = vuelto_restante-10*contar_10
                if (vuelto_restante//5!= 0):
                    contar_5 = vuelto_restante//5
                    vuelto_restante = vuelto_restante-5*contar_5
                    if (vuelto_restante//2!= 0):
                        contar_2 = vuelto_restante//2
                        vuelto_restante = vuelto_restante-2*contar_2
                        if (vuelto_restante==1):
                            contar_1 = vuelto_restante
                           # vuelto_restante = vuelto_restante-contar_1
                          
    #print(vuelto_restante)
    
    if (vuelto_restante//20!= 0):
        contar_20 = vuelto_restante//20
        vuelto_restante = vuelto_restante-20*contar_20
        if (vuelto_restante//10!= 0):
            contar_10 = vuelto_restante//10
            vuelto_restante = vuelto_restante-10*contar_10
            if (vuelto_restante//5!= 0):
                contar_5 = vuelto_restante//5
                vuelto_restante = vuelto_restante-5*contar_5
                if (vuelto_restante//2!= 0):
                    contar_2 = vuelto_restante//2
                    vuelto_restante = vuelto_restante-2*contar_2
                    if (vuelto_restante== 1):
                        contar_1 = vuelto_restante
                       # vuelto_restante = vuelto_restante-contar_1
     
    #print(vuelto_restante)
                        
    if (vuelto_restante//10!= 0):
        contar_10 = vuelto_restante//10
        vuelto_restante = vuelto_restante-10*contar_10
        print(vuelto_restante)
        if (vuelto_restante//5!= 0):
            contar_5 = vuelto_restante//5
            vuelto_restante = vuelto_restante-5*contar_5
            if (vuelto_restante//2!= 0):
                contar_2 = vuelto_restante//2
                vuelto_restante = vuelto_restante-2*contar_2
                if (vuelto_restante==1):
                    contar_1 = vuelto_restante
    
   # print(vuelto_restante)
    if (vuelto_restante//5!= 0):
        contar_5 = vuelto_restante//5
        vuelto_restante = vuelto_restante-5*contar_5
        if (vuelto_restante//2!= 0):
            contar_2 = vuelto_restante//2
            vuelto_restante = vuelto_restante-2*contar_2
            if (vuelto_restante== 1):
                contar_1 = vuelto_restante
    
   # print(vuelto_restante)
    if (vuelto_restante//2!= 0):
        contar_2 = vuelto_restante//2
        vuelto_restante = vuelto_restante-2*contar_2
        if (vuelto_restante==1):
            contar_1 = vuelto_restante
         #   vuelto_restante = vuelto_restante-contar_1
    else: 
        contar_1 = vuelto_restante
     #   vuelto_restante = vuelto_restante-contar_1

    return [contar_50, contar_20, contar_10, contar_5, contar_2, contar_1]   

#print(vuelto(232,290)) # no funciona bien
        
    
    
    
    