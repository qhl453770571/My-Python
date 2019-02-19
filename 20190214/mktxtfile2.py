#!/usr/bin/env python

import os

def get_fname():
    while True:
        fname=input('请输入文件名：')
        if not os.path.exists(fname):
            break
        print('%s已经存在，请重试。' %fname)
    return fname


def get_cotent():
    content=[]

    print('请输入内容，结束请输end')

    while True:
        data=input('>>')
        if data=='end':
            break
        content.append(data)

    return content


def wfile(fname,content):
    with open(fname,'w') as f:
        f.writelines(content)




if __name__ == '__main__':
    fname=get_fname()
    content=get_cotent()
    contents=['%s\n' % line for line in content ]
    print('文件名是：',fname)
    print('内容是：',contents)
    wfile(fname,contents)
