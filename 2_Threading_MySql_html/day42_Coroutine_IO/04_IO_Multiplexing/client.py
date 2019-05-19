import time
import socket
from threading import Thread

def fun():
    skt_c = socket.socket()

    skt_c.connect(('localhost', 8091))
    time.sleep(2)
    skt_c.send(b'Hello')
    msg = skt_c.recv(1024).decode('utf-8')
    print(msg)
    skt_c.close()


for i in range(20):
    Thread(target=fun).start()