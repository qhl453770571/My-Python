#!/usr/bin/env python
#九九乘法表

ind=int(input('请输入乘法表位数：'))

for i in range(1,ind+1):
    for j in range(1,i+1):
        # print(j,'x',i,'=',i*j,end=' ')
        # print(str(j)+'x'+str(i)+'='+str(i*j),end=' ')
        print('%sx%s=%s' %(j,i,j*i),end=' ')
    print()