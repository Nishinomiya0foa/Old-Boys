import socket
sk = socket.socket()

sk.bind(('127.0.0.1', 8080))

sk.listen()

conn,addr = sk.accept()
print(addr)
while True:
    ret = conn.recv(1024).decode()
    print(ret)
    if ret == 'bye':
        conn.send(b'bye')
        break
    # conn.send(bytes('你好', encoding='utf-8'))
    mess = bytes(input('>').encode('utf-8'))
    conn.send(mess)


conn.close()
sk.close()