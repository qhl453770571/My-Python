#!/usr/bin/env python3

import random

all_choice=['石头','剪刀','布']
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]

prompt="""0石头
1剪刀
2布
请选择数字：
"""

cwin=0
pwin=0


while cwin <2 and pwin <2:

    computer=random.choice(all_choice)
    ind=int(input(prompt))
    player=all_choice[ind]

    print("your choice:%s,computer choice:%s" % (player,computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')

    elif [player,computer] in win_list:
        pwin +=1
        print('\033[31;1mYOU WIN!!\033[0m')

    else:
        cwin += 1
        print('\033[31;1mYOU LOSE!!![0m')