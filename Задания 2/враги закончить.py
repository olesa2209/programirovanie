# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:53:51 2023

@author: Pupil
"""

a=['Петя','Маша','Оля','Коля']
b=['Петя','Коля']
c=[]
for i in range (len(a)):
    t= a[i]
    for y in range (len(b)):
        r=b[y]
        if t!=r:
            c.append(t)
print(c)



