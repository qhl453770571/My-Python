#!/usr/bin/env python

username=input('username is:')
password=input('password is:')

if username == 'bob':
    if password == '123456':
        print('login successful')
    else:
        print('login incorrect')
else:
    print('login incorrect')