import socket
import struct

skt_c = socket.socket()

skt_c.connect(('127.0.0.1', 8080))

msg1 = 'Hello'
msg2 = ' Worldxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 先发送msg1 msg2
pack_len = len(msg1+msg2)
pack_len = struct.pack('i', pack_len)

skt_c.send(pack_len)
skt_c.send(msg1.encode('utf-8'))
skt_c.send(msg2.encode('utf-8'))

skt_c.close()

