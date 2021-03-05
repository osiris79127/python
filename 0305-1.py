# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:51:02 2021

@author: USER
"""

number=list()
while len(number)<=5:
    num=int(input('請輸入數字'))
    number.append(num)
number2=number
print('串列內容:',number)
print('氣泡排序法:')
for a in range(6):
    for b in range(a+1,6):        
        if number[a]>number[b]:
            c=number[a]
            number[a]=number[b]
            number[b]=c           
print(number)
d=0
while d<6:
    for e in range(d+1,6):
        if number2[e]<number2[d]:
            c=number2[e]
            number2[e]=number2[d]
            number2[d]=c
    d+=1
print(number2)
