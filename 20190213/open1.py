#!/usr/bin/env python
#open(file,mode,buffering)
#file 文件路径  mode 访问模式   buffering 缓存（默认-1  使用系统默认缓存）

fobj=open('99.py','r')
data=fobj.read()
print(data)
