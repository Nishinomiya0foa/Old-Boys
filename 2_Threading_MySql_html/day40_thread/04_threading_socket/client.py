from threading import Thread
from socket import  socket


def client(c):
    msg = c.recv(1024).decode('utf-8')
    print(msg)
    chat = input('>').encode('utf-8')
    c.send(chat)
    c.close()


if __name__ == '__main__':
    skt_c = socket()
    ip_port = ('localhost', 8099)
    skt_c.connect(ip_port)
    client(skt_c)