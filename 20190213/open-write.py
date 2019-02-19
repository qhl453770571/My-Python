#!/usr/bin/env python

f=open('/root/test.txt','w')
f.write('hello ')
f.flush()  #立即将缓存中的数据同步
f.write('world\n')
f.flush()
# f.read('/root/test.txt')
f.writelines(['2nd line\n','a new line\n'])
f.close()

f=open('/root/test.txt','a')  #如果文件存在请空文件
f.write('wlecome\n')
# f.writelines(['nihao','qiaoxin'])
f.write('nihao\nqiaoxin\n')
f.close()

with open('/root/test.txt','r') as f:
    data=f.read()
    print(data)
print(f.closed) #f.closed为True表示文件对象已关闭