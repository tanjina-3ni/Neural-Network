# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:30:10 2020

@author: Aspire
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([3, 1, 1, 2, 1, 3, 8, 2, 4, 7, 7, 8, 9, 8, 9, 9, 8])
x2 = np.array([5, 4, 6, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])
dt=[0, 7, 15, 4, 10, 6, 10, 10, 5, 1, 9, 1, 2, 0, 8, 0, 0]
#for i in range(0,17):
#    if (x1[i]<=6):
#        dt.append(0)
#    else:
#        dt.append(1)
#print dt

               
w = [0, 9, 17, 6, 2, 8, 12, 7, 3, 1, 9, 10, 20, 2, 8, 2, 2]

   
    
#for i in range(0,17):
#    #x.append(rand.randint(0,10))
#    w.append(rand.randint(0,10))

#print w

    #print y
    #print m
def plott(x,y):
    colors = ['b', 'g']
    markers = ['o', 'v']
    plt.plot()
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.title('Dataset')
    for i in range(0,17):
        if (x1[i]<=6):
            plt.plot(x1[i], x2[i], color=colors[0], marker=markers[0],ls='None')
        else:
            plt.plot(x1[i], x2[i], color=colors[1], marker=markers[1],ls='None')
    
    plt.plot(x1,y)   
    plt.show()



a=1
eta=0.5
while(a==1):
    delta=[]
    y = []
    s=0 
    
    for i in range(0,17):
            s+=x1[i]*w[i]+x2[i]*w[i]
            y.append(s)
    
            #m.append(i)
    for i in range(0,17):
            delta.append(dt[i]-y[i])
   # 
                
    #for i in range(0,17):
            if (y[i]==dt[i]):
                w[i]=w[i]
            elif (y[i]<dt[i]):
                w[i]=w[i]+eta*x1[i]
            else:
                w[i]=w[i]-eta*x1[i]
            #w[i]=w[i]+delta[i]     
    plott(x1,y)
    
            
  
    #print delta
    
    
    
        
    # plot
    


