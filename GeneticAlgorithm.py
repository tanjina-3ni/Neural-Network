# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:17:35 2020

@author: Aspire
"""
import numpy as np
                           #col0 1 2 3 4 5 6 7 8
initialPopulation = np.array([[0,1,0,1,0,1,0,1,1], #row0
                              [0,1,1,1,1,1,0,1,0],    #1
                              [0,1,0,0,1,1,0,1,0],    #2
                              [1,0,0,0,0,0,1,0,1],    #3
                              [1,1,1,1,1,1,1,1,1],    #4 
                              [0,1,0,1,0,1,0,1,0],    #5 
                              [1,0,1,0,1,0,1,0,1],    #6 
                              [1,1,1,1,1,0,0,0,0]])   #7

                #col0 1 2 3 4 5 6 7 8
profit = np.array([[2,1,4,5,0,1,3,5,10], #row0
                   [10,5,1,1,6,1,0,1,0],    #1
                   [0,1,0,4,6,1,4,1,10],    #2
                   [1,0,5,0,4,5,1,0,10],    #3
                   [1,5,1,6,5,10,1,4,1],    #4 
                   [0,1,5,1,0,4,0,1,10],    #5 
                   [1,6,4,0,10,5,1,0,1],    #6 
                   [1,10,1,5,4,5,0,5,0]])   #7

                #col0 1 2 3 4 5 6 7 8
weight = np.array([[20,1,0,1,15,1,0,10,1], #row0
                   [0,10,1,1,15,1,0,4,12],    #1
                   [0,15,0,10,1,5,0,1,20],    #2
                   [1,0,20,5,10,0,15,5,1],    #3
                   [10,1,15,1,5,1,20,1,1],    #4 
                   [6,12,10,1,0,1,20,1,5],    #5 
                   [15,10,1,0,1,0,1,0,15],    #6 
                   [12,1,15,1,1,0,5,20,6]])   #7

def fitness(i):
    ftness = profit[i]*weight[i]
    return ftness
    

#def RouletteWheelSelection:
    

#def onepointCrossover:
    

#def bitFlipMutation:
i=3
print initialPopulation[i]
print profit[i]
print weight[i]
print fitness(i)
