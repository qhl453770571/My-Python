#!/usr/bin/env python

import sys
import subprocess
from randpass1 import gen_pass

def add_user(username,password,fname):
    info="""user information:
username:%s
password:%s
"""

    subprocess.call('useradd %s' % username,shell=True)
    subprocess.call('echo %s | passwd --stdin %s' % (password,username),shell=True)

    with open(fname,'w') as f:
        f.write(info % (username,password))

if __name__ == '__main__':
    username=sys.argv[1]
    password=gen_pass()
    fname='/tmp/userinfo.txt'
    add_user(username,password,fname)