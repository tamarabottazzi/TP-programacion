# -*- coding: utf-8 -*-
"""
Created on Sat May 31 12:59:07 2025

@author: tamar
"""

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4],[2, 0, 3, 5],'ro')
# plt.ylabel('y')
# plt.xlabel('x')
# plt.show()

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
ax.plot(data2, 'd', label='data2')
ax.plot(data3, 'v', label='data3')
ax.plot(data4, 's', label='data4')
ax.legend()


