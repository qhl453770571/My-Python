
import requests

r=requests.get('http://www.baidu.com')
# print(r.text)

print('*'*40)

print(r.encoding)
r.encoding='utf8'
print(r.encoding)

# print(r.text)

url='http://www.weather.com.cn/data/sk/101010100.html'
r=requests.get(url)
bj=r.json()
print(bj)
print('*'*40)
print(bj['weatherinfo'])
print('*'*40)
print(bj['weatherinfo']['SD'])

