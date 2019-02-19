#!/usr/bin/env python

# import random
# import string
from random import choice
from string import ascii_letters,digits

all_chs=ascii_letters+digits

def randpass(n=8):
    result=[choice(all_chs) for i in range(n)]
    return ''.join(result)

if __name__ == '__main__':
    print(randpass())
    print(randpass(4))