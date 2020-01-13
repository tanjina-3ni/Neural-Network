# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:24:54 2020

@author: Aspire
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
y = np.array([5, 4, 6, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])
g= np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def distance(x1,x2,y1,y2):
    p=float((x1-x2)**2)
    q=float((y1-y2)**2)
    s=float((p+q)**0.5)
    return s

i1=x[1]
j1=y[1]
i2=x[12]
j2=y[12]
print(i1,j1)
plt.plot()
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('Dataset')
plt.scatter(x,y)
plt.show()

# create new plot and data
plt.plot()
X = np.array(list(zip(x, y))).reshape(len(x), 2)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']



# KMeans algorithm 
#r=0

while (1):
    
    s1=0
    s2=0
    t1=0
    t2=0
    j=0
    c=0
    for i in range(0,16):
        a=distance(x[i],i1,y[i],j1)
        b=distance(x[i],i2,y[i],j2)
        
        
        if (a<b):
            s1=s1+x[i]
            s2=s2+y[i]
            c=c+1
            g[i]=1
            
        else:
            t1=t1+x[i]
            t2=t2+y[i]
            j=j+1
            g[i]=0
   
    
    s1=s1/c
    s2=s2/c
    
    t1=t1/j
    t2=t2/j
    if i1 == s1 and j1 == s2 and i2 == t1 and j2 == t2:
            break
    
    else:
            i1=s1
            j1=s2
            i2=t1
            j2=t2
print("C1(x,y)")
for i in range(0,16):
    if(g[i]==1):
        print("({},{})".format(x[i], y[i]))

print("\nC2(x,y)")
for i in range(0,16):
    if(g[i]==0):
        print("({},{})".format(x[i], y[i]))


         

plt.plot()
for i, l in enumerate(g):
    plt.plot(x[i], y[i], color=colors[l], marker=markers[l],ls='None')
    plt.xlim([0, 10])
    plt.ylim([0, 10])

plt.show()
 