# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 08:58:11 2023

@author: Pupil
"""


lst = [1, 2, 3, 4, 5, 6]
def change(lst):
    first = lst[0]
    last = lst[-1]
    lst[0] = last
    lst[-1] = first
    return lst

print(change(lst))