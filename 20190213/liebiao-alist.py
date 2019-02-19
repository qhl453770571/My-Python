#!/usr/bin/env python
#将1-10之间的整数放入列表
# alist=[]
#
# for i in range(1,10):
#     alist.append(i)
# print(alist)

alist = [i for i in range(1,11)]
alist2 = [i for i in range(1,11) if i%2 == 0]
alist3 = [5+5 for i in range(10)]
print(alist)
print(alist2)
print(alist3)