import socket
import time
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 还可以有这种写法
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            command = data.decode('utf-8')
            if not data:
                break
            if command == 'date':
                conn.sendall(time.ctime().encode('utf-8'))
            elif command == 'os':
                conn.sendall(os.name.encode('utf-8'))
            elif command == 'ls':
                conn.sendall(os.curdir.encode('utf-8'))