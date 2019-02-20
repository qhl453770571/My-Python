#!/usr/bin/env python3

class BearToy:
    def __init__(self,size,color):
        self.size=size
        self.color=color

    def speak(self):
        print('hahaha')

if __name__ == '__main__':
    tidy=BearToy('small','orange')
    print(tidy.size)
    tidy.speak()