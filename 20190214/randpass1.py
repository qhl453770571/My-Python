#!/usr/bin/env python

from string import digits,ascii_letters
from random import choice

all_chs=digits+ascii_letters+'_'

def gen_pass(n=8):

    password=''

    for i in range(n):
        ch=choice(all_chs)
        password+=ch
    return password

if __name__ == '__main__':
    print(gen_pass())
    # print(gen_pass(4))
