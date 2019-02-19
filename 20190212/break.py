#!/usr/bin/env python
#练习  要求输入用户名 当用户输入用户名不是tom 就一直输入
uname=input('请输入用户名：')
while uname != 'tom':
    uname=input('请继续输入用户名：')