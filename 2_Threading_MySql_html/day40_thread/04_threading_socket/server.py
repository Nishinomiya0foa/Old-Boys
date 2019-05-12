from socket import socket
from threading import Thread


def server(c, a):
    want = input('>').encode('utf-8')
    c.send(want)
    msg = c.recv(1024)
    print(a, msg.decode('utf-8'))


if __name__ == '__main__':
    skt_s = socket()
    ip_port = ('', 8099)
    skt_s.bind(ip_port)
    skt_s.listen()
    while True:
        conn, addr = skt_s.accept()
        thr = Thread(target=server, args=(conn, addr))
        thr.start()