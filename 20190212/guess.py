#!/usr/bin/env python
#猜数字游戏
#随机生存一个数字  用户猜数字  提示大了/小了/对了
import random
#randint(min,max) 生成min-max的随机整数
answer =int(input('guess a number (1~100):'))
num = random.randint(1,100)
print('电脑输出:',num)
if answer < num:
    print('猜小了')
elif answer > num:
    print('猜大了')
else:
    print('猜对了')