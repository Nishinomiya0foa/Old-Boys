# 基于TCP协议实现远程执行命令
# server端下发命令



# 基于UDP协议 默写基础的网络通信
import socket

skt_udp = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8080)

skt_udp.bind(ip_port)

ret, addr = skt_udp.recvfrom(1024)

print(ret.decode('utf-8'))

skt_udp.close()