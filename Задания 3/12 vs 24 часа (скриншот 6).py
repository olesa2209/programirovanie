# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:03:43 2023

@author: Pupil
"""

a=int(input())
s=str(a)
f=':00'
b=input('')
print(s+b)
if b=='am':
    print('24-часовой формат - '+s+f)
else:
    g=a+12
    y=str(g)
    print('24-часовой формат - '+y+f)