#!/usr/bin/env python3

stack=[]

def push_it():
    item=input('item to push:')
    stack.append(item)


def pop_it():
    if stack:
        print('\033[31;1mPopped%s\033[0m' % stack.pop())
    else:
        print('\033[31;1mEmpty stack\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    promp="""(0)push_it
(1)pop_it
(2)view_it
(3)quit
please input your choice(0/1/2/3):"""

    cmds={'0':push_it(),'1':pop_it(),'2':view_it()}

    while True:
        choice=input(prompt).strip()[0]
        if choice not in '0123':
            print('ivalid input,Try again.')
            continue
        if choice == '3':
            break

        cmds
