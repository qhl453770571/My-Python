
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass


def send_email(text,sender,receivers,subject,host,user,passwd):
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP(host)
    smtp.login(user, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())


if __name__ == '__main__':

    text='这是一封python测试邮件\r\n'
    sender='qihl06105212@163.com'
    receivers=['qihl06105212@163.com']
    subject='python test'
    host='smtp.163.com'
    user='qihl06105212@163.com'
    passwd=getpass.getpass()
    send_email(text,sender,receivers,subject,host,user,passwd)