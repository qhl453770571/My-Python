#!/usr/bin/env python

with open('/root/test.txt') as f:
    print(f.tell())
    f.readline()
    print(f.tell())

#seek(offset,whence)
#whence有三个值  0开头  1当前   2结尾
    f.seek(5,0)   #起点位置0   移动5个偏移量
    print(f.tell())