#!/usr/bin/env python

with open('/tmp/passwd','a') as f:
    print(f.tell())
    f.seek(0,0)
    f.write('nsd1809')
    print(f.tell())

f=open('/tmp/passwd')
data=f.readlines()
print(data)
print(f.tell())

