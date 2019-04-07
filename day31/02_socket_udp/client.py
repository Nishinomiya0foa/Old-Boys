import socket
skt_udp = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8080)

skt_udp.sendto(b'Hello', ip_port)

ret, addr = skt_udp.recvfrom(1024)
print(ret.decode('utf-8'))

skt_udp.close()
