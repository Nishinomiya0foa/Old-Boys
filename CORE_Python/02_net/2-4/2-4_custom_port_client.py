import socket

def place_tcp(ip, port):
    skt_c = socket.socket()
    skt_c.connect((ip,port))
    skt_c.send(b'Hello')
    print(skt_c.recv(1024).decode('utf-8'))
    skt_c.close()

def place_udp(ip, port):
    skt_c = socket.socket(type=socket.SOCK_DGRAM)
    ip_port = (ip, port)
    print(ip_port)
    skt_c.sendto(b'Hello', ip_port)
    ret, addr = skt_c.recvfrom(1024)
    print(ret.decode('utf-8'))

if __name__ == '__main__':
    ip = input('IP:')
    port = input('PORT:')
    try:
        port = int(port)
    except ValueError:
        print('ValueError!')

# place_tcp(ip, port)
place_udp(ip, port)




