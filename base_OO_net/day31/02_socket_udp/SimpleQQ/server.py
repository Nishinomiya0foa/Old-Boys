import socket

skt_ser = socket.socket(type=socket.SOCK_DGRAM)
myIpPort = ('127.0.0.1', 8080)

skt_ser.bind(myIpPort)

while True:
    # 接收信息
    msg, addr = skt_ser.recvfrom(1024)
    print(msg.decode('utf-8'))

    # 发送信息
    beg = input('server >')
    beg = '服务器：'+beg
    beg.encode('utf-8')
    skt_ser.sendto(beg, addr)

skt_ser.close()
