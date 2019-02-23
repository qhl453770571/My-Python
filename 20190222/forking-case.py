#!/usr/bin/env python3

import os
import time
from datetime import datetime

pid=os.fork()

if pid:
    print('in parent')
    time.sleep(5)
    print('parent exit')

else:
    for i in range(5):
        print(datetime.now())
        time.sleep(2)
    print('child exit')




