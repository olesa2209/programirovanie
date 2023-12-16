# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:38:22 2023

@author: Pupil
"""

a='вика тоже собака'
def VIKA(a):
    while 'а' in a:
        a=a.replace('а','4')
    while 'е' in a:
        a=a.replace('е','3')
    print(a)
VIKA(a)