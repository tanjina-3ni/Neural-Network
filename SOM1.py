# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:05:12 2020

@author: Aspire
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


row = 5
col = 5
noOfInput = 3
noOfOutput = row*col

weights = np.random.uniform(size=(noOfOutput,noOfInput))
plt.figure(figsize=(1,1))
circleSide = 0.5

size = 5
ax = plt.axes([0,0,size,size])
plt.axis((0,5*circleSide,0,5*circleSide))

for i in range(row*col):
        xy = circleSide*np.array([np.floor(i/row) + 0.5, (col-1-i)%col + 0.5])
        color = tuple(weights[i,:])
        circle = mpatches.Ellipse(xy, circleSide, circleSide, color = color)
        plt.gca().add_patch(circle)