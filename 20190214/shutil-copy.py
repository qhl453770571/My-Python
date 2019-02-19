#!/usr/bin/env python3
import shutil

# with open('/etc/passwd','rb') as src_file:
#     with open('/tmp/mima','wb') as dst_file:
#         shutil.copyfileobj(src_file,dst_file)
#
# shutil.copyfile('/etc/passwd','/tmp/mima1')
#
# shutil.copy('/etc/passwd','/tmp/')
#
# shutil.copy2('/etc/passwd','/root/')
#
# shutil.move('/tmp/passwd','/var/')

# shutil.copytree('/root/python1809/20190214','/tmp/day4')
# shutil.rmtree('/tmp/day4')

# shutil.copymode('/etc/shadow','/tmp/passwd')
shutil.copystat('/etc/shadow','/tmp/passwd')
# shutil.chown('/tmp/passwd',user='Student',group='Student')