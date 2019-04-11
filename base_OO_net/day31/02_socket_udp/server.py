import socket
# 获取udp的socket对象
sk_udp = socket.socket(type=socket.SOCK_DGRAM)  # DGRAM datagram  数据报文

sk_udp.bind(('127.0.0.1', 8080))

# 必须等待client先发信息
msg, addr = sk_udp.recvfrom(1024)  # udp中用recvfrom
print(msg.decode('utf-8'))

sk_udp.sendto(b'bye', addr)

sk_udp.close()
