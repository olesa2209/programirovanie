# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:30:53 2023

@author: Pupil
"""

a=input()
b=input()
if a==b:
    print('ничья')
else:
    if a=='бумага':
        if b=='камень':
            print('игрок 1 выйграл')
        else:
            print('игрок 2 выйграл')
    if a=='камень':
        if b=='бумага':
            print('игрок 2 выйграл')
        else:
            print('игрок 1 выйграл')
    if a=='ножницы':
        if b=='бумага':
            print('игрок 1 выйграл')
        else:
            print('игрок 2 выйграл')