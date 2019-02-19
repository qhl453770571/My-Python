

def mygen():

    yield 'hello qiaoxin'
    a=10+20
    yield a
    yield [1,2,3]

a=mygen()

print(a.__next__())
print(a.__next__())
print(a.__next__())

# b=mygen()
#
# for item in b:
#     print(item)