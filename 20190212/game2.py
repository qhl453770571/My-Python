#!/usr/bin/env python
#剪刀石头布小游戏
#电脑随机出  玩家自己决定
import random
#列出所有选择
all_choise=['剪刀','石头','布']
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
computer=random.choice(all_choise)  #随机出
#为玩家提供一个选择菜单
prompt='''[0]剪刀
[1]石头
[2]布
请选择(0/1/2):
'''
ind=int(input(prompt))  #将玩家输入的数字作为索引值 从all_choise中取对应的选择 如ind=0 all_choise[ind]='剪刀'
player=all_choise[ind]
print('电脑选择'+computer,'你的选择'+player)
if computer==player:
    print('平局')
elif [player,computer] in win_list:
    print('你赢了')
else:
    print('你疏了')