
import os
import time


ret_val=os.fork()
if ret_val:
    print('父进程')
    time.sleep(5)
    # result = os.waitpid(-1,0)
    result = os.waitpid(-1, 1)
    print(result)
    time.sleep(20)
    print('父进程结束')

else:
    print('子进程')
    time.sleep(30)
    print('子进程结束')
    exit()

