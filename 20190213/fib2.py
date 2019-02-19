#!/usr/bin/env python

def gen_fib(l):
    fib=[0,1]

    for i in range(l-len(fib)):
        fib.append(fib[-1]+fib[-2])

    return fib
    # print(fib)

a=gen_fib(10)
print(a)

print('*'*50)

n=int(input('数列长度：'))
print(gen_fib(n))