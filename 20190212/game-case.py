#!/usr/bin/env python

import random

player=int(input('请输入数字 0剪刀 1石头 2布：'))

computer = random.randint(0,2)

if (player==0 and computer == 2) or (player==1 and computer==0) or (player==2 and computer==1):
    print('you win!!')

elif player==computer:
    print('平局')
else:
    print('you lose！！')