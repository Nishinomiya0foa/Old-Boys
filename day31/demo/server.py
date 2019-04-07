import socket

# tcp协议
sk1 = socket.socket()    # 实例化一个socket对象
sk1.bind(('127.0.0.1', 8080))  # 给server端绑定一个ip和端口
sk1.listen()  # 监听

flag = 0
while True:
    flag+= 1
    conn, addr = sk1.accept()  # 获取到一个client连接，已经连接好了。说明已经完成了3次握手
                            # 阻塞
    # 之后通信是使用 conn
    while True:
        msg = conn.recv(1024).decode('utf-8')  # 阻塞，直到收到一个客户端发来的消息
        print(msg)
        if msg == 'bye':
            conn.send(b'bye')
            break
        beg = bytes(input('>'),encoding='utf-8')
        conn.send(beg)

    conn.close()   # 关闭长连接
    if flag == 2:
        break
sk1.close()  # 关闭socket对象