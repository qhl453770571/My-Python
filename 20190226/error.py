
from urllib.error import HTTPError
from urllib.request import urlopen

url1 = 'http://127.0.0.1/abc/'
url2 = 'http://127.0.0.1/ban/'

try:
    html = urlopen(url1)
except HTTPError as e:
    print('错误:', e)

print('*' * 40)

try:
    html = urlopen(url2)
except HTTPError as e:
    print('错误:', e)

