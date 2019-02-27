
from urllib.request import urlopen
from urllib.request import Request

header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

url='http://www.teud.cn'

html=Request(url,headers=header)


data=urlopen(html)

print(data)

# a=list(data)
# print(a)