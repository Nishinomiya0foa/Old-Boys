import socket

sk = socket.socket()  # 实例化一个socket对象
sk.connect(('127.0.0.1', 8080))  # 连接地址

while True:
    mess = bytes(input('>'), encoding='utf-8')
    sk.send(mess)

    ret = sk.recv(1024).decode()  # 接收信息并解码   decode() 从bytes解码
    print(ret)
    if ret == 'bye':
        sk.send(b'bye')
        break


sk.close()