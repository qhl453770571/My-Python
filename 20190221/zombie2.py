

import os
import time

pid=os.fork()
if pid:
    print('父进程')
    result=os.waitpid(-1,0)
    print(result)
    time.sleep(20)
    print('父进程结束')

else:
    print('子进程')
    time.sleep(30)
    print('子进程结束')
    exit()