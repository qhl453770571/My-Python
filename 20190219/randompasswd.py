#!/usr/bin/env python3

from random import choice
from string import ascii_letters,digits

all_ch=ascii_letters+digits+'_'


def randpass(n=8):
    result = [choice(all_ch) for i in range(n)]
    return ''.join(result)

if __name__ == '__main__':
    print(randpass())