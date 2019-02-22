
import socket

from time import strftime

class TcpTimeServ:
    def __init__(self,host,port):
        self.addr=(host,port)
        self.serv=socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
        self.serv.bind=(self.addr)
        self.serv.listen(1)

    def chat(self,cli_sock):
        while True:
            data=cli_sock.recv(1024)
            data=data.decode()
            if data.strip()='quit':
                break



    def mainloop(self):
        while True:
            cli_sock,cli_addr=self.serv.accept()
            self.chat(cli_sock)
            cli_sock.close()

