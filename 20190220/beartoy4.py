#!/usr/bin/env python3

class Bear:
    def __init__(self,color,size):
        self.color=color
        self.size=size

    def sing(self):
        print('My color is %s' % self.color)

class NewBear(Bear):
    def __init__(self,name,color,size):
        super(NewBear,self).__init__(color,size)
        self.name=name

    def run(self):
        print('i can run ......')

if __name__ == '__main__':
    bear1=NewBear('xiaonbig','Brown','Middle')
    bear1.sing()