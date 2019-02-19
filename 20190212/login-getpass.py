#!/usr/bin/env python

#调用函数可以在命令行窗口无回显输入
import getpass

username = input('your username is:')
password = getpass.getpass('your password is:')

if username == 'bob' and password == '123456':
    print('\033[32;1mlogin successful!\033[0m')
else:
    print('\033[31;1mlogin incorrect!\033[0m')