#!/usr/bin/env python3

class Bear:
    def __init__(self,color,size):
        self.color=color
        self.size=size

    def sing(self):
        print('My color is %s' % self.color)


if __name__ == '__main__':
    bear_big=Bear('Red','large')
    print(bear_big.color,bear_big.size)
    bear_big.sing()

    bear2=Bear('brown','Middle')
    print(bear_big.color,bear_big.size)
    bear2.sing()