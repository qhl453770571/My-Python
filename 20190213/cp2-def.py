#!/usr/bin/env python
#模拟复制cp操作

import sys

def copy(src,dst):

    f1=open(src,'rb')

    f2=open(dst,'wb')


    while True:
        data=f1.read(4096)
        if not data:
            break
        f2.write(data)

    f1.close()
    f2.close()

copy(sys.argv[1],sys.argv[2])

