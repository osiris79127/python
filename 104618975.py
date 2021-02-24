# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:44:59 2021

@author: USER
"""

number=int(input('數字'))
a=0
b=list()
c=list()
for i in (range(1,number+1)):
    if i%2==0:
        a+=i
        b.append(i)
    else:
        c.append(i)
print(a)
print('偶數:',b)
print('奇數:',c)