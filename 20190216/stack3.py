#!/usr/bin/env python3


stack=[]

def push_it():
    item=input('输入要添加的：')
    stack.append(item)

def pop_it():
    if stack:
        print('\033[31;1mPoped %s\033[0m' % stack.pop())
    else:
        print('\033[32;1mEmpty stack!\033[0m')


def view_it():
    print('\033[33;1m%s\033[0m' % stack)


def show_menu():
    prompt="""(0)push
(1)pop
(2)view
(3)quit
please input your choice(0/1/2/3):"""

    cmds={'0':push_it,'1':pop_it,'2':view_it}

    while True:
        choice=input(prompt).strip()
        if choice not in ['0','1','2','3']:
            print('\033[31;1mIvalid choice. Try again!\033[0m')
            continue
        if choice == '3':
            break
        else:
            cmds[choice]()
        # elif choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_it()


if __name__ == '__main__':
    show_menu()

