#!/usr/bin/env python
#模拟复制cp操作

#打开/bin/ls 作为源文件
f1=open('/bin/ls','rb')
#打开/root/ls作为目标文件
f2=open('/root/ls','wb')
#重复的从源文件读取内容到目标文件

while True:
    data=f1.read(4096)  #建议每次读取一部分内容
    if not data:
        break
    f2.write(data)

# 关闭文件
f1.close()
f2.close()


