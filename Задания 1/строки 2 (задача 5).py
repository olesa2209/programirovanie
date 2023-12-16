# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:33:33 2023

@author: Pupil
"""

a='текст текст текст (текстик) текст'
b='(текстик)'
def Vika(a,b):
    c=a.find(b)
    print(c)
    if c!=-1:
        v=a.replace(b,'')
        print(v)
    else: 
        print('ghffjhj')
Vika(a,b)