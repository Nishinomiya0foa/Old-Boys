import socket
import hmac
import os

skt = socket.socket()
skt.bind(('localhost', 8091))

print(socket.gethostname())
print(socket.gethostbyname_ex(socket.gethostname()))

skt.listen(0)

conn, addr = skt.accept()
print('Connent Client：{}'.format(addr))


def check_client(conn):
    msg = os.urandom(32)
    conn.send(msg)
    h = hmac.new(msg, b'dan')
    secret_h = h.digest()
    ret = conn.recv(1024)
    return hmac.compare_digest(ret,secret_h)


compared = check_client(conn)
if compared:
    print('合法客户端')
    while True:
        ques = conn.recv(1024).decode('utf-8')
        if ques != 'q':
            ans = ques.strip('吗').strip('?').strip('？')
            ans = ans + '。'
            conn.send(ans.encode('utf-8'))
        else:
            break
else:
    print('不合法客户端')

conn.close()
skt.close()



conn.close()
skt.close()