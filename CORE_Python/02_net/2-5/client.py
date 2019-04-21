import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        command = input('command:')
        if not command:
            break
        s.send(command.encode('utf-8'))
        data = s.recv(1024)
        print('Received', repr(data))

