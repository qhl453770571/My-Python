#!/usr/bin/env python3
#
# name=input('请输入姓名：')
#
# age=input('请输入年龄：')
#
# print('%s is %s years old' %(name,age))

# print('%s is %s years old' %('bob',23))
#
# print('%s is %d years old' %('bob',23))
#
# print('%s is %f years old' %('bob',23.5))
#
# print('%s is %5.2f years old' %('bob',23.5))  #宽度5  2位小数

# print('%5s%5s' %('name','age'))   #5为宽度  正数右对齐
# print('%-5s%-5s' %('name','age'))  #5为宽度  负数左对齐
#
# print('%010d' % 123)  #0表示位数补0

# print('{} is {} years old'.format('bob',23))
#
# print('{1} is {0} years old'.format('bob',23))
#
# print('{:<010} is {:^08} years old'.format('bob',23))  #0表示补齐 <左对齐 >右对齐 ^居中

print('{0[0]} is {0[1]} years old'.format(['bob','23']))










