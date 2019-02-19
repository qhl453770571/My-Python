#!/usr/bin/env python3

def func1(x):
    if x == 1:
        return x
    return x * func1(x-1)

if __name__ == '__main__':
    print(func1(3))
    print(func1(6))