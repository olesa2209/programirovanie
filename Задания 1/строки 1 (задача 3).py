# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:31:23 2023

@author: Pupil
"""

a='Обломов лежал лежал лежал и устал'
from collections import Counter
def sona(a):
    f = Counter(a.replace(' ','')).most_common(3)
    print(f)
sona(a)