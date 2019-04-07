import socket

sk2 = socket.socket()

sk2.connect(('127.0.0.1', 8080))

while True:
    beg = bytes(input('>'), encoding='utf-8')
    sk2.send(beg)

    msg = sk2.recv(1024).decode('utf-8')
    print(msg)
    if msg == 'bye':
        sk2.send(b'bye')
        break

sk2.close()