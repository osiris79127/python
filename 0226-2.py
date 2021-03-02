# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:34:44 2021

@author: OSIRIS
"""


a=10
while a>0:
    for i in range(1,a):
        print(i,sep='',end='')
    a-=1
    print()
    
for b in range(10,0,-1):
    for c in range(1,b):
        print(c,sep='',end='')
    print()