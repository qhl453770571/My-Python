#!/usr/bin/env python3
import os

# os.getcwd()
#
# os.chdir('/tmp')
# os.getcwd()
#
# os.mkdir("example")
#
# os.chdir('/tmp/example')
#
# os.getcwd()
#
# f=os.open('test.txt',os.O_RDWR|os.O_CREAT)
# os.write(f,b'nihao  qiaoxin')
#
# os.listdir('/tmp/example')
#
# os.lseek(f,0,0)
#
# str=os.read(f,100)
#
#
# str=bytes.decode(str)
#
# print('读取的字符是：',str)
#
# os.close(f)

os.remove('/tmp/example/test.txt')

os.removedirs('/tmp/example')




# print(os.symlink('/etc/hosts','zj'))

