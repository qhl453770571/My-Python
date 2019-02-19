#!/usr/bin/env python

from random import randint

num=randint(1,10)

counter=0

while counter<5:
    answer=int(input('来猜一个数(1-10)：'))
    if answer>num:
        print('猜大了')
    elif answer==num:
        print('猜对了')
        break
    else:
        print('猜小了')
    counter+=1
else:
    print('这个数字是：',num)
