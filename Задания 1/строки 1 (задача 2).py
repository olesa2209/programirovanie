# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:30:20 2023

@author: Pupil
"""

a='всем приветикиприв'
b=[]
c='прив'
s='нет ничего'
def vika():
    q=a.find(c)
    if q==-1:
        b.append(s)
    else:
        b.append(q)
    w=a.rfind(c)
    if w!=-1:
        b.append(w)
    print(b)
vika()