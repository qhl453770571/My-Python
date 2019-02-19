#
# adict={'father':'haile','daugter':'qiaoxin'}
# print(adict)
#
# bdict=dict((['father','haile'],['mother','linlin']))
# print(bdict)
#
alist=[10,100,50]
# print(alist)
# for ind,val in enumerate(alist):
#     print('index:%s,%s' %(ind,val))

alist.append(200)
print(alist)

alist.insert(1,300)
print(alist)

alist.reverse()
print(alist)

alist.sort()
print(alist)

alist.reverse()
print(alist)

alist.sort(reverse=True)
print(alist)

alist.pop(-1)
print(alist)


alist.append(100)
print(alist)

c=alist.count(100)
print(alist)
print(c)

alist.remove(300)
print(alist)

x=alist.index(100)
print(x)


