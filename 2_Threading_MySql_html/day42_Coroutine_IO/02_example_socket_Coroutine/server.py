from gevent import monkey;monkey.patch_all()
from socket import socket
import gevent

skt_s = socket()
ip_port = ('', 8091)
skt_s.bind(ip_port)
skt_s.listen(1)

def task(conn, addr):
    conn.send(b'Hello')
    msg = conn.recv(1024).decode('utf-8')
    print(addr,':',msg)
    conn.close()

while True:
    conn, addr = skt_s.accept()
    gevent.spawn(task, conn, addr[1])
skt_s.close()