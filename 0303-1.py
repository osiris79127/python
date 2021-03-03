# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:40:10 2021

@author: USER
"""

import random
count=1
ans=random.randint(1,100)
guess=int(input('請輸入1-100間的數字:'))
min=1
max=100
if ans==guess:
    print('一次就猜對')
while ans!=guess: 
    if ans>guess:
        min=guess
        guess=int(input('請輸入:{}到:{}的數字'.format(min,max)))
        count+=1
    if ans<guess:
        max=guess
        guess=int(input('請輸入:{}到:{}的數字'.format(min,max)))
        count+=1
    if ans==guess:
        print('猜對了,共猜了',count,'次')
        break