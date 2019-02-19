#!/usr/bin/env pthon3

import string
import keyword

first_chs=string.ascii_letters+'_'
all_chs=string.digits+first_chs

def check_id(idt):
    if idt[0] not in first_chs:
        return '第一个字符不合法'

    for ind,ch in enumerate(idt[1:]):
        if ch not in all_chs:
            return '第{}个字符的{}非法'.format(ind+2,ch)

    if keyword.iskeyword(idt):
        return '{}是关键字，不能用作自定义标识符'.format(idt)

    return '{}是合法的标示符'.format(idt)

if __name__ == '__main__':
    idt = input('请输入要检查的标示符：')
    a=check_id(idt)
    print(a)



