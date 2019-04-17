from socket import *

skt = socket()

ip_port = ('localhost', 8091)

skt.connect(ip_port)

skt.send(b' Hi')

skt.close()