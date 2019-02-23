#!/usr/bin/env python3

import os
import time

pid=os.fork()

if pid:
    print('父进程')
    # time.sleep(15)
    result=os.waitpid(-1,1)
    print(result)
    time.sleep(2)
    print('父进程结束')

else:
    print('子进程')
    time.sleep(10)
    print('子进程结束')
    exit()