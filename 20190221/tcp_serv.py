
import socket

host=''
port=12345
addr=(host,port)
s=socket.socket()  #默认创建TCP套接字

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(addr)
s.listen(1)
cli_sock,cli_addr=s.accept()
data=cli_sock.recv(1024)
print(data)
print(data.decode())
sdata='吃了么?\r\n'

cli_sock.send(sdata.encode())
cli_sock.close()
s.close()

