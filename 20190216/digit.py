#!/usr/bin/env python3

a=input('输入字符串：')

for i in a:
    if i not in '1234567890':
        print('不全是数字')
        break
    else:
        print('全是数字')