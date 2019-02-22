#!/usr/bin/env python3

def count_patt(fname,patt):
    cpatt=re.compile(patt)
    patt_dict={}
    with open(fname) as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                key=m.group()
                # if key not in patt_dict:
                #     patt_dict[key]=1
                # else:
                #     patt_dict[key]+=1
                patt_dict[key]=patt_dict.get(key,0)+1
    return patt_dict


if __name__ == '__main__':
    fname='access_log'
    ip='^(\d+\.){3}\d+'
    print(count_patt(fname,ip))
    br="Firefox|Chrome|MSIE"
    print(count_patt(fname,br))
    print(count_patt('/etc/passwd','bash$|nologin$'))