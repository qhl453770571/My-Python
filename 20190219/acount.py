#!/usr/bin/env python3

import os
import pickle
from time import strftime

def init_data(record):

    """数据的形式[时间，收入，开销，余额，备注]
    ['2019-2-19',0,0,10000,'init']

    """
    data=[
        [strftime('%Y-%m-%d'),0,0,10000,'init']
    ]
    with open(record,'wb') as fobj:
        pickle.dump(data,fobj)


def save(record):
    amount=flout(input('金额：'))
    comment=input('备注：')
    date=strtime('%Y-%m-%d')
    with open(record,'rb') as fobj:
        record_list=pickle.load(fobj)
    balance=record_list[-1][-2]+amount
    record_list.append([date,amount,0,balance,comment])
    with open(record,'wb') as fobj:
        pickle.dump(record_list,fobj)


def cost(record):
    amount=flout(input('金额：'))
    comment=input('备注：')
    date=strtime('%Y-%m-%d')
    with open(record,'rb') as fobj:
        record_list=pickle.load(fobj)
    balance=record_list[-1][-2]-amount
    record_list.append([date,0,amount,balance,comment])
    with open(record,'wb') as fobj:
        pickle.dump(record_list,fobj)


def query(record):
    with open(record,'rb') as fobj:
        record_list=pickle.load(fobj)

        print('%-14s%-10s%-10s%-12s%-20s' % ('date','save','cost','balance','comment'))

        for record in record_list:
            print('%-14s%-10s%-10s%-12s%-20s' % tuple(record))


def show_menu():
    prompt="""(0)收入
(1)开销
(2)查询
(3)退出
请选择(0/1/2/3):"""

    cmds={'0':save,'1':cost,'2':query}
    record='record.data'
    if not os.path.exists(record):
        init_data(record)
    while True:
        choice=input(prompt).strip()
        if choice not in [str(i) for i in range(4)]:
            print('无效的出入，请重试！')
            continue
        if choice =='3':
            print('\nbyebye')
            break

        cmds[choice]()




if __name__ == '__main__':
    show_menu()





