#!/usr/bin/env python

#通过参数获取函数外的数据  交给函数处理  返回结果
def mysum(a,b):   #定义函数时写的参数称为形式参数  简称形参
    return a+b

x=mysum(10,20)  #在调用函数时传递的参数称为实际参数  简称实参
print(x)