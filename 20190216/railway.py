#!/usr/bin/env python3

import time,sys

l=19

counter=0

print('#'*(l+1),end='')

while True:
    # sys.stdout.flush()
    print('\r%s@%s' %('#'*counter,'#'*(l-counter)),end='')
    time.sleep(2)
    counter+=1

    if counter==l:
        counter=0