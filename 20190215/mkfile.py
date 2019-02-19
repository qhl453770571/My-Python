#!/usr/bin/env python3

import os

def get_fname():
    while True:
        fname=input('请输入文件名：')
        if not os.path.exists(fname):
            break
        print('%s已存在，请重试' % fname)

    return fname


def get_contents():
    contents=[]

    print('请输入内容，以end结束')
    while True:
        line = input('>')
        if line == 'end':
            break
        contents.append(line)
    return contents


def wfile(fname,contents):
    with open(fname,'w') as f:
        f.writelines(contents)


if __name__ == '__main__':
    fname=get_fname()
    contents=get_contents()
    contents=['%s\n' % line for line in contents]
    wfile(fname,contents)