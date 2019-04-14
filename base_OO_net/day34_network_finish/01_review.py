# TCP中，
# sendall， 尝试一次发送所有数据，成功返回None，失败抛异常

# socket.setblocking()  设置套接字的阻塞与非阻塞模式


import socket

skt = socket.socket()

# 设置全局不阻塞
skt.setblocking(False)

skt.bind(('localhost', 8091))

skt.listen()

try:
    # 如果设置了不阻塞， 在这儿没有接受到连接时，会报错。
    conn, addr = skt.accept()
except BlockingIOError:
    pass

print('ddddddddd')