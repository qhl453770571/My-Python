import os

# print('starting')
# os.fork()
# print('hello world!')

print('starting')
ret_val=os.fork()

if ret_val:
    print('hello parents')
else:
    print('hello child')

print('hello both')