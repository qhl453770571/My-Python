#!/usr/bin/env python3

from random import randint

def qsort(seq):

    if len(seq) < 2:
        return seq

    midlle=seq[0]
    smaller=[]
    larger=[]

    for item in seq[1:]:
        if item < midlle:
            smaller.append(item)
        else:
            larger.append(item)
    return qsort(smaller)+[midlle]+qsort(larger)

if __name__ == '__main__':
    nums=[randint(1,100) for i in range(10)]
    print(nums)
    print(qsort(nums))

