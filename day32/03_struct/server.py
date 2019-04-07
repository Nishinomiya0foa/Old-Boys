import socket
import struct

skt_s = socket.socket()

skt_s.bind(('127.0.0.1', 8080))

skt_s.listen()

conn, addr = skt_s.accept()

pack_len = conn.recv(4)
pack_len = struct.unpack('i', pack_len)
print('pack_len:',pack_len)
ret = conn.recv(pack_len[0])

# 这样会出现黏包
# ret = conn.recv(7)

print(ret.decode('utf-8'))

conn.close()
skt_s.close()