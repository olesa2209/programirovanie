# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:28:06 2023

@author: Pupil
"""

a=[1,2,3,4]
b=[5,6,7,8]
c=[]
def Vika(a,b,c):
    for i in range (len(a)):
        h = a[i]
        k = b[i]
        g = str(h)+';'+str(k)
        c.append(g)
    print(c) 
Vika(a,b,c)    
