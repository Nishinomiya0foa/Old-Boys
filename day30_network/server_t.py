import socket
import time

sk = socket.socket()  # 实例化一个socket对象

sk.bind(('127.0.0.1', 8080))  # 绑定一个端口

sk.listen()  # 时刻接收报文

conn, addr = sk.accept()

while True:
    ret = conn.recv(1024)
    # print(ret.decode())
    if ret.decode() == 'EXIT':
        conn.send(b'EXIT')
        break
    ret = float(ret.decode())
    timeArray = time.localtime(ret)
    s_t = time.strftime('%H:%M:%S', timeArray)
    conn.send(bytes('当前时间为 {}'.format(s_t), encoding='utf-8'))


conn.close()
sk.close()



