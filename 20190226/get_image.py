
import os
import re


from urllib.request import urlopen

def download(url,fname):
    html=urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data=html.read(1024)
            if not data:
                break
            fobj.write(data)

def get_url(fname,patt,encoding='utf8'):
    patt_list=[]
    cpatt=re.compile(patt)
    with open(fname,encoding=encoding) as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                patt_list.append(m.group())

    return patt_list




if __name__ == '__main__':
    path='/tmp/myimg'
    if not os.path.exists(path):
        os.mkdir(path)
    url_163='http://www.tmooc.cn/'

    fname_163=os.path.join(path,'163.html')
    download(url_163,fname_163)

    img_patt='(http|https)://[-/.\w]+\.(png|jpg|jpeg|gif)'
    img_list=get_url(fname_163,img_patt)

    # print(img_list)

    for url in img_list:
        fname=url.split('/')[-1]
        fname=os.path.join(path,fname)
        download(url,fname)









