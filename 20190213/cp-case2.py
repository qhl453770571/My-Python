#!/usr/bin/env python3

src='/bin/ls'
dst='/root/ls'

f1=open(src,'rb')
f2=open(dst,'wb')

while True:
    data=f1.read(4096)
    if data == b'':
        break
    f2.write(data)

f1.close()
f2.close()