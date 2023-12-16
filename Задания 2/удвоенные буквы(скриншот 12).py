# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:14:50 2023

@author: Pupil
"""

a='рассказывать'
def Vika(a):
    for i in range(len(a)-1): 
        s=a[i]
        c=a[i+1]
        if s==c:
            print('True')
Vika(a)