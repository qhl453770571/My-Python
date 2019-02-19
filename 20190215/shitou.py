#!/usr/bin/env python3

import random

all_choice = ['石头','剪刀','布']
win_list=[['石头','剪刀'],['布','石头'],['剪刀','布']]
prompt="""(0)石头
(1)剪刀
(2)布
请选择数字："""

cwin=0
pwin=0
ping=0

while cwin<2 and pwin<2:
    print('三局两胜，再来!')
    ind=int(input(prompt))
    player=all_choice[ind]
    computer=random.choice(all_choice)

    print('你的选择是%s,电脑选择是%s' % (player,computer))

    if [player,computer] in win_list:
        print('你赢了')
        pwin+=1
    elif player==computer:
        print('平局')
        ping+=1
    else:
        print('你输了')
        cwin+=1



if cwin>pwin:
    print('最终computer赢了，一共比了%s局,电脑赢了%s局' % (pwin+cwin+ping,cwin))
else:
    print('最终你赢了，一共比了%s局，你赢了%s局' % (pwin+cwin+ping,pwin))