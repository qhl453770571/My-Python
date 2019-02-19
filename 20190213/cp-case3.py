#!/usr/bin/env python3

src='/bin/ls'
dst='/root/ls'

with open(src,'rb') as f1:
    with open(dst,'wb') as f2:
        while True:
            data=f1.read(4096)
            if not data:
                break
            f2.write(data)
