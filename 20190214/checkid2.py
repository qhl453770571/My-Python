#!/usr/bin/env python

#检测标示符是否合法
#标识符要求  首字母必须为_或大小写字母
#后续字符可以为数字字母和_
#标示符不能为关键字
#输出第几个标识符不合法

import string,keyword

first_chs=string.ascii_letters+'_'
all_chs=first_chs+string.digits

def check_id(idt):
    if idt[0] not in first_chs:
        return '您输入的第1个字符不合法'

    for ind,ch in enumerate(idt[1:]):
        if ch not in all_chs:
            return '您输入的第%s个字符的%s非法' %(ind+2,ch)

    if keyword.iskeyword(idt):
        return '%s是关键字，不能作为自定义的标示符' %idt

    return '%s是合法的标示符' %idt

if __name__ == '__main__':
    idt=input('请输入要检查的字符：')
    print(check_id(idt))