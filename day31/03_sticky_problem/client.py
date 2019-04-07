# client端执行命令

import socket

skt_client = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8080)

skt_client.sendto(b'Hi', ip_port)

skt_client.close()