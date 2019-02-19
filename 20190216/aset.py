#
# aset=set('abc')
# print(aset)

# bset=set('cde')
# print(bset)

# cset=set('hello')
# print(cset)
#
# print(len(cset))
#
# for ch in cset:
#     print(ch)
#
# dset=aset | bset
# print(dset)
#
# eset=aset & bset
# print(eset)

# fset=aset-bset
# print(fset)

# aset.add(('hello'))
# print(aset)
#
# aset.add('world')
# print(aset)

# aset.update(['qiaoxin','nihao'])
# print(aset)
#
# bset={'a','b','c'}
#
# a=bset.issubset(aset)
# print(a)
#
# b=aset.issuperset(bset)
# print(b)
#
# print(aset.union(bset))
# print(bset.union(aset))
#
# print(aset.intersection(bset))
#
# print(aset.difference(bset))
# print(bset.difference(aset))


import random
# print([random.randint(1,20) for i in range(20)])
# print(set([random.randint(1,20) for i in range(20)]))

alist =[random.randint(1,20) for i in range(20)]
print(alist)

aset=set(alist)
print(aset)

blist=list(aset)
print(blist)





