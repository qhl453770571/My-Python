#!/usr/bin/env python
#模拟复制cp操作

f1=open('/bin/ls','rb')
f2=open('/tmp/ls','wb')

data=f1.read()
f2.write(data)

f1.close()
f2.close()
