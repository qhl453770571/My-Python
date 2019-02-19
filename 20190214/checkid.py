#!/usr/bin/env python

import string
import keyword

first_chs=string.ascii_letters+'_'
all_chs=first_chs+string.digits

def check_id(idt):
    if idt[0] not in first_chs:
        return '第1个字符不合法'

    for ind,ch in enumerate(idt[1:]):
        if ch not in all_chs:
            return '第%s个字符的%s非法' %(ind+2,ch)

    if keyword.iskeyword(idt):
        return '%s是关键字，不能作为自定义的标示符' %idt

    return '%s是合法的标示符' %idt

if __name__ == '__main__':
    idt=input('请输入代检察的标示符：')
    print(check_id(idt))



