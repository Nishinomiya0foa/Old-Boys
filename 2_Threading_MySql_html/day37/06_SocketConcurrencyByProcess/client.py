from socket import socket

skt_c = socket()
ip_port = (
    'localhost', 8091
)
skt_c.connect(ip_port)

msg = skt_c.recv(1024).decode('utf-8')
print(msg)

ret = input('>')
skt_c.send(ret.encode('utf-8'))

skt_c.close()