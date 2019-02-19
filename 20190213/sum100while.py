#!/usr/bin/env python
#求1-100之间整数累加

counter=0
sum100=0

while counter<100:
    counter += 1
    if counter % 2 == 1:
        continue  #遇到奇数跳过
    sum100+=counter

print(sum100)
