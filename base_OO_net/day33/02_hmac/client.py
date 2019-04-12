import socket
import hmac

skt = socket.socket()

skt.connect(('127.0.0.1', 8091))

msg = skt.recv(1024)

h = hmac.new(msg, b'dan')

secret_h = h.digest()

skt.send(secret_h)

while True:
    ques = input('>').encode('utf-8')
    skt.send(ques)
    ans = skt.recv(1024).decode('utf-8')
    if ques.decode('utf-8') != 'q':
        print(ans)
    else:
        break

skt.close()