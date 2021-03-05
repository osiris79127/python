# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:16:18 2021

@author: USER
"""

import random
#1
b=list()
c=0
while c<6:
    a=random.randint(1,49)
    if b.count(a)==0:
        b.append(a)
        c+=1
print(b)
#2
d=list()
for i in range(1,50):
    if d.count(i)==0:
        d.append(i)  
h=list()
e=0
while e<6:
    f=random.randint(1,49)
    if h.count(f)==0:
        h.append(f)
        e+=1
print(h)