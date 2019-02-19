#!/usr/bin/env python

from random import randint

num=randint(1,10)

time=5

print("-----欢迎来到猜数字游戏，请开始-----")

while time > 0:
    guess=int(input('请输入0-10之间的数字：'))
    print('你数入的数字是：',guess)

    if 0<guess<10:
        if guess==num:
            print('猜对了')
            break
        else:
            print('不对,你还剩',time-1,'次机会')
        time-=1
    else:
        print('输入非法，重新来：')
print('游戏结束，正确结果是：',num)