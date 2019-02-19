#!/usr/bin/env python

import random

answer=int(input('guess a number 1~100:'))
num=random.randint(1,100)
print('电脑输出：',num,'你的输出：',answer)
if answer < num:
    print('你猜小了')
elif answer > num:
    print('你猜大了')
else:
    print('你猜对了')
