#!/usr/bin/env python3

import os

def get_fname():
    while True:
        filename=input('please input filename:')
        if not os.path.exists(filename):
            break
        print('%salready exist,please try again' % filename)

    return filename

def get_contents():
    contents=[]

    print('please input contents,end with input end.')
    while True:
        line=input('>')
        if line=='end':
            break
        contents.append(line)
    return contents

def wfile(fname,contents):
    with open(fname,'w') as f:
        f.writelines(contents)


if __name__ == '__main__':
    fname=get_fname()
    contents=get_contents()
    # contents=['%s\n' % line for line in contents]
    wfile(fname,contents)
