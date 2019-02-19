#!/usr/bin/env python3

import random

all_choice = ['石头','剪刀','布']
win_list=[['石头','剪刀'],['布','石头'],['剪刀','布']]
prompt="""(0)石头
(1)剪刀
(2)布
请选择数字："""

ind=int(input(prompt))
player=all_choice[ind]
computer=random.choice(all_choice)

cwim
print('你的选择是%s,电脑选择是%s'% (player,computer))

if [player,computer] in win_list:
    print('你赢了')
elif player==computer:
    print('平局')
else:
    print('你输了')