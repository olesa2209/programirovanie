# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 09:45:39 2023

@author: Pupil
"""

a='ttppfkfj??????'
b=''
for i in range(len(a)):
    c=a[i]
    b=b+c
    if a[i+1]=='!':
        b=b+'!'
        break
    if a[i+1]=='?':
        b=b+'?'
        break
print(b)
    