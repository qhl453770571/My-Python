
import os
import time
from datetime import datetime

pid=os.fork()
if pid:
    print('in parent')
    time.sleep(10)
    print('parent exit')

else:
    for i in range(5):
        print(datetime.now())
        time.sleep(1)
    print('child exit')