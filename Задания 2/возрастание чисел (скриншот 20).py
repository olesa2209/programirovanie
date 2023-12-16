# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:47:02 2023

@author: Pupil
"""

n=[1,2,3,5,10,8]
m=0
def Vika(n,m):
    for i in range(len(n)-1):
        if n[i]<n[i+1]:
            m=m+1
    if m>=(len(n)-1):
        print('возрастает')
    else:
        print('не возрастает')
Vika(n,m)