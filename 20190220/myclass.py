#!/usr/bin/env python3

class MyClass1:
    def hello(self):
        print('hello world')

    def greet(self):
        print('class1')


class MyClass2:
    def welcome(self):
        print('How are you!')

    def greet(self):
        print('class2')

class C(MyClass2,MyClass1):
    pass
    # def greet(self):class C(MyClass2,MyClass1):

    #     print('in C')


if __name__ == '__main__':
    mc=C()
    mc.hello()
    mc.welcome()
    mc.greet()