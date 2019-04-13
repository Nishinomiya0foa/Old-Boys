import socket

skt = socket.socket()

skt.connect(('localhost',8808))

skt.send(b'Hello')

print(skt.recv(1024).decode('utf-8'))

skt.close()