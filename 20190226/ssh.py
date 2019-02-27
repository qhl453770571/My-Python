
import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.4.5',username='root',password='123456')

# ssh.exec_command('mkdir /tmp/mydemo')

result=ssh.exec_command('id root;id qihaile')
print(result[2].read())
print(len(result))

ssh.close()