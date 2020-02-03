# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:00:46 2020

@author: Aspire
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def outputPlot(weight,noOfrow,noOfcol):
    plt.figure(figsize=(1,1))
    c=0.5
    size = 5
    plt.axes([0,0,size,size]) # correct the size of ractangle
    plt.axis((0,5*c,0,5*c)) # shows x,y coordinate values

    for i in range(noOfoutput):
        xy = c*np.array([np.floor(i/noOfrow) + 0.5, (noOfcol-1-i)%noOfcol + 0.5])
        color = tuple(weight[i,:]) #RGB color
        circle = mpatches.Ellipse(xy, c, c, color = color) #to draw circle
        plt.gca().add_patch(circle)
    plt.show()


def train(noOfpatterns,patterns,weight):
    
    eta=0.3
    for i in range(100):
        for i in np.random.permutation(noOfpatterns):
            inputs = patterns[i,:]
            distance = np.sqrt(np.power(inputs-weight,2).sum(axis=1))
            winner = distance.argmin()
            weight=weight+eta*(inputs-weight)
    return weight
        
   
           


noOfrow=5
noOfcol=5
noOfinput=3
noOfoutput=noOfrow*noOfcol
weight = np.random.uniform(size=[noOfoutput,noOfinput]) # every circle(total 25 or noOfoutput) has 3(noOfinput) values
#print weight

outputPlot(weight,noOfrow,noOfcol)
#plt.show()


sigma0=0.5
lamda=100
t=np.arange(100) # prints 0-99 inegers in an array
sigma=sigma0*np.exp(-t/lamda)

#print sigma

noOfpatterns = 40*40
patterns = np.random.uniform(size=(noOfpatterns,noOfinput))
#print patterns

train(noOfpatterns,patterns,weight)
outputPlot(weight,noOfrow,noOfcol)



