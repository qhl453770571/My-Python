
import requests

url='http://oimagea4.ydstatic.com/image'

r=requests.get(url)

with open ('/tmp/m.jpg','wb') as fobj:
    fobj.write(r.content)

