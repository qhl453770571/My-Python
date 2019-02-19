#!/usr/bin/env python

from mktxtfile import get_contents

width=48

content=get_contents()

print('+%s+' %('*'*48))

for line in content:
    print('+{:^48}+'.format(line))


print('+{}+'.format('*'*48))