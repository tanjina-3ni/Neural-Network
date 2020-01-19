# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 09:01:24 2020

@author: Aspire
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 08:21:52 2020

@author: Aspire
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:24:54 2020

@author: Aspire
"""
import numpy as np
import matplotlib.pyplot as plt
import random
#x = np.array([3, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
#y = np.array([5, 4, 6, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])
x=[]
y=[]
for z in range(0,20):
    x.append(random.randrange(0, 15))
for z in range(0,20):
    y.append(random.randrange(0, 15))

g= np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def distance(x1,x2,y1,y2):
    p=float((x1-x2)**2)
    q=float((y1-y2)**2)
    s=float((p+q)**0.5)
    return s

i1=x[1]
j1=y[1]
i2=x[12]
j2=y[12]
i3=x[9]
j3=y[9]
#print(i1,j1)
plt.plot()
plt.xlim([0, 20])
plt.ylim([0, 20])
plt.title('Dataset')
plt.scatter(x,y)
plt.show()

# create new plot and data
#plt.plot()
#X = np.array(list(zip(x, y))).reshape(len(x), 2)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']



# KMeans algorithm 
#r=0

while (1):
    
    s1=0
    s2=0
    t1=0
    t2=0
    u1=0
    u2=0
    d=0
    j=0
    c=0
    for i in range(0,16):
        a=distance(x[i],i1,y[i],j1)
        m=distance(x[i],i3,y[i],j3)
        b=distance(x[i],i2,y[i],j2)
        
        
        if (a<b and a<m):
            s1=s1+x[i]
            s2=s2+y[i]
            c=c+1
            g[i]=1
        elif (m<a and m<b):
            u1=u1+x[i]
            u2=u2+y[i]
            d=d+1
            g[i]=2
            
        elif (b<a and b<m):
            t1=t1+x[i]
            t2=t2+y[i]
            j=j+1
            g[i]=0
   
    #if c!=0:
    s1=s1/c
    s2=s2/c
    
    #if d!=0:
    u1=u1/d
    u2=u2/d
    #if j!=0:
    t1=t1/j
    t2=t2/j
    if i1 == s1 and j1 == s2 and i2 == t1 and j2 == t2 and i3 == u1 and j3 == u2:
            break
    
    else:
            i1=s1
            j1=s2
            i2=t1
            j2=t2
            i3=u1
            j3=u2
            
print("C1(x,y)")
for i in range(0,20):
    if(g[i]==1):
        print("({},{})".format(x[i], y[i]))

print("\nC2(x,y)")
for i in range(0,20):
    if(g[i]==0):
        print("({},{})".format(x[i], y[i]))

print("\nC3(x,y)")
for i in range(0,20):
    if(g[i]==2):
        print("({},{})".format(x[i], y[i]))


         

plt.plot()
plt.title('Output')
for i, l in enumerate(g):
    plt.plot(x[i], y[i], color=colors[l], marker=markers[l],ls='None')
    plt.xlim([0, 20])
    plt.ylim([0, 20])

plt.show()
 