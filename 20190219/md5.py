

import hashlib

m=hashlib.md5(b'123456')

print(m.hexdigest())

with open('/etc/passwd','rb') as fobj:
    data=fobj.read()

m=hashlib.md5(data)

print(m.hexdigest())