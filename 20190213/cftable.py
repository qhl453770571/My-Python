#!/usr/bin/env python

num=int(input('请输入位数：'))
for i in range(num+1):
    for j in range(1,i+1):
        print('%sx%s=%s' % (j,i,j*i),end=' ')
    print()
