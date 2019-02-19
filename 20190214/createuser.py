#!/usr/bin/env python

import subprocess
from randpass1 import gen_pass


#useradd
#echo pwd | passwd --stdin user

def adduser(user,pwd,fname):
    subprocess.call('useradd %s' % user,shell=True)
    subprocess.call('echo %s | passwd --stdin %s' % (pwd,user),shell=True)

    with  open(fname,'a') as f:
        f.write('user:%s,pwd:%s\n' % (user,pwd))

if __name__ == '__main__':
    user=input('请输入要创建的用户名：')
    pwd=gen_pass()
    adduser(user,pwd,'/tmp/user_info')

