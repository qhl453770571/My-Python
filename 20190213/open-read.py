#!/usr/bin/env python

f=open('/root/test.txt','r')  #默认就是r打开
data1=f.read()
f.close()

f=open('/root/test.txt','r')
data2=f.read(10)
f.close()

f=open('/root/test.txt')
data3=f.readline(4)  #从指针开始读这行4个字节
data4=f.readline()  #从指针开始读一行的剩余内容
data5=f.readlines()  #从指针开始读剩余的所有行的内容  返回列表  每行为一个元素
f.close()

# print(data1)
# print('*'*20)
print(data2)  #前面已经把文件全部打开   此时指针在文件最后
print('*'*20)
print(data3)
print(data4)
print('*'*20)
print(data5)