#!/usr/bin/env python
#使用列表生成斐波那切数列

def gen_fib(num):

    fib=[0,1]

    for i in range(num-2):
        fib.append(fib[-1]+fib[-2])
    # return fib
    print(fib)

gen_fib(5)