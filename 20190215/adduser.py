#!/usr/bin/env python

import sys
import subprocess
from randpass import gen_pass

def add_user(username,password,fname):
    info="""---用户信息如下---
用户名：%s
密码：%s
"""

    subprocess.call('useradd %s' %username,shell=True)
    subprocess.call('echo %s | passwd --stdin %s' %(password,username),shell=True)

    with open(fname,'w') as f:
        f.write(info %(username,password))

if __name__ == '__main__':
    username=sys.argv[1]
    password=gen_pass()
    fname='/root/usersinfo.txt'
    add_user(username,password,fname)

