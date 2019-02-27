
from urllib import request

# html=request.urlopen('http://www.baidu.com')
#
# data=html.read()
#
# with open('/tmp/bd.html','wb') as fobj:
#     fobj.write(data)


def download(url,fname):
    html=request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data=html.read(1024)
            if not data:
                break
            fobj.write(data)



if __name__ == '__main__':
    download('http://cdn.tmooc.cn/bsfile//imgad///D188E62C70FF40EDA8C4DB961778B361.png','/tmp/danei')




