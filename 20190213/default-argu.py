#!/usr/bin/env python
#位置传参

import sys
# print(sys.argv)   #位置参数列表  默认第一项为脚本文件自身
def p_star(num=10):  #定义默认值
    print('*'*num)

p_star(20)  #定义默认参数  这里可以不写  如果写了  以这里为准