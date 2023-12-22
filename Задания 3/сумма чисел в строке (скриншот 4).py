# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 22:31:35 2023

@author: Алексей
"""


a='ghjfb3j4j56h7'
def Vika(a):
    b=0
    c=''
    for i in a:
        t=i.isdigit()
        if t==True:
            c+=i
        else:
            if c!='':
               b+=int(c)
               c=''
    b+=int(c)
    print(b)
Vika(a)        
        