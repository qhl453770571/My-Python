#!/usr/bin/env python

#字符串内建函数
#调用方式  字符串.函数

py_str='     HELLO wo2rld     '
print(py_str)
#
# print(py_str.capitalize())
# print(py_str.title())
#
# print(py_str.center(20,'*')) #在20个字符串内居中   默认补空格  指定*
# print(py_str.center(20,'0'))
#
# print(py_str.ljust(20,'*'))
# print(py_str.rjust(20,'*'))
#
# print(py_str.count('l'))  #统计l出现的次数
## print(py_str.strip())  #去除左右两侧的空白
# print('   nihao qiaoxin   '.strip())
#
# print(py_str.upper())  #将字符串全部转成大写

# print(py_str.count('o',2,4)) #统计从下标2到4范围内出现o的次数
#
# print(py_str.startswith('h'))  #判断字符串是否以h开头
# print(py_str.endswith('d')   #判断结尾是否d
# print(py_str.endswith('s'))

#
# print(py_str.islower())  #是否全部小写（只判断字母）
# print(py_str.isupper())   #是否是全部是大写
#
#
# print(py_str.isdigit())  #是否为数字
# print(py_str.isalnum())  #是否为数字字母
# print(py_str.isalpha())  #是否为字母


# print(py_str.strip())  #去除左右两侧的空白
# print('   nihao qiaoxin   '.strip())
#
# print(py_str.upper())  #将字符串全部转成大写

print(py_str.lower())  #转成小写

print('nihao.qiaoxin'.split('.'))  #指定.位分割符['nihao', 'qiaoxin']

print(py_str.split())  #分割 默认是空格  返回['HELLO', 'wo2rld']

print('.'.join(['ni','hao','qiaoxin']))  #返回ni.hao.qiaoxin