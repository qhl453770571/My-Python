#!/usr/bin/env python3

hi='hello world'

def pstar(num):
    print('*'*num)

# 当模块文件直接执行时,__name__的值为'__main__'
if __name__ == '__main__':
    pstar(20)
