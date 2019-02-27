from urllib import request
import json
import pprint

url='http://www.weather.com.cn/data/sk/101010100.html'
r=request.urlopen(url)
data=r.read()
print(type(data))
print('*'*20)

bj=json.loads(data)
print(type(bj))
print('*'*20)
pprint.pprint(bj)
pprint.pprint(bj['weatherinfo'])

