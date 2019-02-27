
import requests

url='http://www.kuaidi100.com/query'
params={'type':'zhongtong','postid':'75130646677839'}
r=requests.get(url,params=params)
print(r.json())



