import socket

skt_user1 = socket.socket(type=socket.SOCK_DGRAM)

server_ip_port = ('127.0.0.1', 8080)

while True:
    # 发送的消息
    beg = input('user1 >')
    beg = 'use1:'+beg
    beg.encode('utf-8')
    skt_user1.sendto(beg, server_ip_port)

    msg, addr = skt_user1.recvfrom(1024)
    print(msg.decode('utf-8'))

skt_user1.close()