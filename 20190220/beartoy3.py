#!/usr/bin/env python3

class Bear:
    def __init__(self,color,size):
        self.color=color
        self.size=size

    def sing(self):
        print('My color is %s' % self.color)

class NewBear(Bear):
    pass

if __name__ == '__main__':
    bear1=NewBear('Brown','Middle')
    bear1.sing()