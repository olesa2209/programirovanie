# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:42:31 2023

@author: Pupil
"""
a='1, 2, 4, 5'
f=1
b=[]
def Vika(a,f):
   for i in range(len(a)):
       if a[i]!=" " and a[i]!=",":
           n=int(a[i])
           b.append(n)      
   print(b)   
   for i in b:
       f=f*i
   print(f)
Vika(a,f)