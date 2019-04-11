import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

flag = 0
while True:
    if flag > 5:
        sk.send(b'EXIT')
        break
    t = time.time()
    sk.send(bytes(str(t), encoding='utf-8'))

    ret = sk.recv(1024)
    print(ret.decode())

    time.sleep(10)
    flag += 1

sk.close()