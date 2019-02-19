#!/usr/bin/env python3

import getpass

userdb={}

def register():
    username=input('请输入用户名:')
    if username in userdb:
        print('\033[31;1m%s 已经存在,请重试.\033[0m' % username)
    else:
        password=getpass.getpass('请输入密码:')
        userdb[username]=password


def login():
    while True:
        username=input('请输入用户名:')
        password=getpass.getpass('请输入密码:')
        # if username in userdb and userdb[username]==password:
        if userdb.get(username)==password:
            print('\033[32;1m登陆成功\033[0m')
            break
        else:
            print('\033[31;1m登陆失败,请重试!\033[0m')


def show_menu():
    cmds={'0':register,'1':login}
    prompt="""(0)注册
(1)登陆
(2)退出
(3)查看用户列表
请做出选择(0/1/2/3):"""

    while True:
        choice=input(prompt).strip()
        if choice not in ['0','1','2','3']:
            print('\033[31;1m无效选择,请重试\033[0m')
            continue
        elif choice == '2':
            break
        elif choice == '3':
            print(userdb)
            continue
        else:
            cmds[choice]()


if __name__ == '__main__':
    show_menu()