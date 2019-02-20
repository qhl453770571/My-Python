
import re
#
# a=re.match('f..','food')
# print(a.group())
#
#
# b=re.findall('f..','seafood is food')
# print(b.group())
#
# re.finditer('f..','seafood is food')
# a=list(re.finditer('f..','seafood is food'))
# print(a)
# print(a.group)

# print(re.match('f..','seafood'))

a=re.split('\.|-','hello-world.tar.gz')
print(a)

a=re.sub('x','zs','Hi x. nice to meet you,x.')
print(a)

patt=re.compile('f..')
m=patt.search('seafood os food')
print(m.group())

n=patt.findall('seafood is food')
print(n)