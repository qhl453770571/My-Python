#!/usr/bin/env python

import random

all_choice=['剪刀','石头','布']
winlist=[['剪刀','布'],['石头','剪刀'],['布','石头']]
prompt="""(0)剪刀
（1）石头
（2）布
please input your choise:
"""

computer=random.choice(all_choice)
ind=int(input(prompt))
player=all_choice[ind]

print("your choice:",player,";computer choise:",computer)

if computer == player:
    print("平局")
elif [player,computer] in winlist:
    print("you win!")
else:
    print("you lose!!")
