#!/usr/bin/env python3

import random

num=random.randint(1,100)
print(num)
isrunning=True

while isrunning:
    answer=int(input('guess a number(1~100):'))
    if answer<num:
        print('猜小了')
    elif answer>num:
        print('猜大了')
    else:
        print('猜对了')
        isrunning=False