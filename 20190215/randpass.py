#!/usr/bin/env python

from random import choice
from string import ascii_letters,digits

all_chs=ascii_letters+digits+'_'

def gen_pass(n=8):
    result=[choice(all_chs) for i in range(n)]
    return ''.join(result)
    # return result

if __name__ == '__main__':
    [print(randpass())]
