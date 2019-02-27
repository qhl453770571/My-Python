
import requests

r1=requests.get('http://127.0.0.1')

print(r1.status_code)

url='http://127.0.0.1/abc'

r2=requests.get(url)

print(r2.status_code)
