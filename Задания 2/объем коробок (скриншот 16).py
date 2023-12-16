# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:52:50 2023

@author: Pupil
"""

a=[1, 3, 4]
b=[2, 4, 6]
d=[8, 9, 1]
f=1
g=1
u=1
def Vika(a,b,d,f,g,u):
    for i in a:
        f=f*i
    for i in b:
        u=u*i
    for i in d:
        g=g*i
    v=f+u+g
    print(v)
Vika(a,b,d,f,g,u)