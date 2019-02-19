#!/usr/bin/env python3

import random

num=random.randint(1,100)
print(num)
isrunning=True
roundnum=1
a=''

while roundnum<6:
    answer=int(input('guess a number(1~100):'))
    if answer<num:
        print('猜小了')
    elif answer>num:
        print('猜大了')
    else:
        a='ok'
        print('猜对了，共猜了',roundnum,'次')
        break
    roundnum+=1

if a != 'ok':
    print('超过5次，没机会了，这个数字是：',num)