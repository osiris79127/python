# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:34:44 2021

@author: OSIRIS
"""


for i in range(5):
    print(' '*(5-i)+'*'*(2*i-1))
for i in range(5,0,-1):
    print(' '*(5-i)+'*'*(2*i-1))
for i in range(1,5):
    print(' '*(5-i),end='')
    print(str(2*i-1)*(2*i-1))
for i in range(5,0,-1):
    print(' '*(5-i),end='')
    print(str(2*i-1)*(2*i-1))