#!/usr/bin/env python3

from mkfile import get_contents

contents=get_contents()

width=int(input('输入宽度：'))
print('+%s+' %('*'*width))
for line in contents:
    print('+{:^48}+'.format(line))

print('+%s+' %('*'*width))
