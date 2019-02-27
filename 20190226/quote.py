
from urllib.request import quote,unquote

url='http://www.sogo.com/web?query='
word=quote('达内')

print(word)

print(url+word)

code=unquote('%E8%BE%BE%E5%86%85')
print(code)