#!/usr/bin/env  python3

import random


all_choice=['石头','剪刀','布']
win-list=[['石头','剪刀'],['剪刀','布'],['布','石头']]


prompt='''0石头
1剪刀
2布
请选择数字：
'''

computer = random.choice(all_choices)

ind = int(input(prompt))
player = all_choices[ind]
print('你出了：%s,计算机出的是：%s' %(player,computer))

if player == computer:
    print('\033[32;1m平局\033[0m')

elif [player, computer] in win_list:
    print('\033[31;1mYou WIN!!!\033[0m')

else:
    print('\033[31;1mYou LOSE!!!\033[0m')