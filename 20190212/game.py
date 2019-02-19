#!/usr/bin/env python
#剪刀石头布小游戏
#电脑随机出  玩家自己决定
import random
#列出所有选择
all_choise=['剪刀','石头','布']
computer=random.choice(all_choise)  #随机出
player=input('请选择：')

if player == '剪刀':
    if computer == '石头':
        print('you lose')
    elif computer == '布':
        print('you win')
    else:
        print('平局')
elif player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '布':
        print('you lose')
    else:
        print('you win')
else:
    if computer == '石头':
        print('you win')
    elif computer == '布':
        print('平局')
    else:
        print('you lose')