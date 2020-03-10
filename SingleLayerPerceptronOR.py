# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:30:10 2020

@author: Aspire
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = [0,0,1,1]
x2 = [0,1,0,1]
dt=[0.0, 1.0, 1.0, 1.0]

#for i in range(0,17):
#    if (x1[i]<=6):
#        dt.append(0)
#    else:
#        dt.append(1)
#print dt

               
w1 = [1,1,1,1]
w2=[1,1,1,1]


   
    
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
    plt.xlim([-1,3])
    plt.ylim([-1, 3])
    plt.title('Dataset')
    for i in range(0,4):
        if (dt[i]==0):
            plt.plot(x1[i], x2[i], color=colors[0], marker=markers[0],ls='None')
        else:
            plt.plot(x1[i], x2[i], color=colors[1], marker=markers[1],ls='None')
    
    plt.plot(y,x)   
    plt.show()



a=1
count=0
#eta=0.5

while(a!=0):
    delta=[]
    y = []
    y0 = []
    s=0 
    
    for i in range(0,4):
            s+=x1[i]*w1[i]+x2[i]*w2[i]
            y.append(s)
    
            #m.append(i)
    for i in range(0,4):
         w1[i]=w1[i]+0.5*(dt[i]-y[i])
         w2[i]=w2[i]+0.5*(dt[i]-y[i])
            #delta.append(dt[i]-y[i])
   # 
                
    #for i in range(0,17):
    count=count+1
    x=[1.0,0.0,0.0,0.0]
    
    plott(x,y) 
    
    print dt,y
    if dt==y:
        a=0
        print "No of iteration: ",count
        break
    
   
            
             
    
    
    #a=a+1
            
  
    #print delta
    
    
    
        
    # plot
    


