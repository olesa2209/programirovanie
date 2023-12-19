# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:53:51 2023

@author: Pupil
"""

a=['Петя','Маша','Оля','Коля']
b=['Петя','Коля']
def vika(a,b):
    for i in range (len(b)):
        if a.count(b[i])>0:
           a.remove(b[i])
vika(a,b)
print(a)




