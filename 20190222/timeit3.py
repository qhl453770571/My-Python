import time
import os
import threading

def add(n=20000000):
    result=0
    for i in range(n):
        result+=i
    print(result)

if __name__ == '__main__':
    start=time.time()

    # for i in range(5):
    #     add()


    # for i in range(5):
    #     pid=os.fork()
    #     if not pid:
    #         add()
    #         exit()


    tlist=[]
    for i in range(5):
        t=threading.Thread(target=add)
        t.start()







    end=time.time()
    print(end-start)