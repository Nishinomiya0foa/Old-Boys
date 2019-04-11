import socket
import time

skt_1 = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8080)

beg = '%Y-%m-%d  %H:%M:%S'.encode('utf-8')

flag = 0

while True:
    skt_1.sendto(beg, ip_port)

    msg, addr = skt_1.recvfrom(1024)
    print(msg.decode('utf-8'))

    time.sleep(5)
    flag += 1

    if flag == 7:
        break
skt_1.close()