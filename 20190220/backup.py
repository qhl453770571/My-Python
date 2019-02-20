import os
import tarfile
from time import strftime
import pickle
import hashlib

def check_md5(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest




def full_backup(src,dest,md5file):
    fname=os.path.basename(src.rstrip('/'))
    fname='%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
    fname=os.path.join(dest,fname)

    tar=tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()

    md5dict={}
    for path,folder,files in os.walk(src):
        for file in files:
            full_path=os.path.join(path,file)
            md5_dict[full_path]=check_md5(full_path)
    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)


def incr_backup(src,dest,md5file):
    fname = os.path.basename(src.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    with open(md5file,'rb') as fobj:
        old_md5=pickle.load(fobj)

    new_md5={}
    for path, folder, files in os.walk(src):
        for file in files:
            full_path = os.path.join(path,file)
            new_md5[full_path] = check_md5(full_path)

    tar=tarfile.open(fname,'w:gz')
    for key in new_md5:
        if old_md5.get(key) != new_md5[key]:
            tar.add(key)
    tar.close()


    with open(md5file,'wb') as fobj:
        pickle.dump(new_md5,fobj)


if __name__ == '__main__':
    src='/tmp/mydemo/security/'
    dest='/tmp/mydemo/'
    md5file='/tmp/mydemo/md5.data'

    if strftime('%a')=='Mon':
        full_backup(src,dest,md5file)
    else:
        incr_backup(src,dest,md5file)

