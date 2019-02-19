#!/usr/bin/env python
#求1-100之间整数累加

# counter=0
sum100=0

for counter in range(2,101,2):
    # counter += 2
    # if counter % 2 == 1:
    #     continue  #遇到奇数跳过
    sum100+=counter

print(sum100)
