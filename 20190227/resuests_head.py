
import requests

headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}

r=requests.get('http://127.0.0.1',header=headers)

print(r.status_code)

