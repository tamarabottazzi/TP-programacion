# -*- coding: utf-8 -*-
"""
Created on Thu May 22 10:26:12 2025

@author: tamar
"""

import funcion_meteo

maximas = [20, 10, 34, 0, 0]

minimas = [33, 0, 12, 0, 0]


# for i in range(5):
#     maximas.extend([float(input(f"máxima día {i+1}: "))])
#     minimas.extend([float(input(f"mínima día {i+1}: "))])    

print(funcion_meteo.meteo(maximas,minimas))
