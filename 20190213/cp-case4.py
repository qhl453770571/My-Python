#!/usr/bin/env python3

import sys

def copy(src,dst):
    with open(src,'r') as f1:
        with open(dst,'w') as f2:
            while True:
                data=f1.read(4096)
                if not data:
                    break
                f2.write(data)

copy(sys.argv[1],sys.argv[2])