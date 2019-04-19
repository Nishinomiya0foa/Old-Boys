import socket

def place_tcp():
    skt_s = socket.socket()

    ip_port = ('localhost', 8091)

    skt_s.bind(ip_port)

    skt_s.listen(5)

    conn, addr = skt_s.accept()

    ret = conn.recv(1024).decode('utf-8')

    print(ret)

    conn.send(ret.upper().encode('utf-8'))

    conn.close()

def place_udp():
    skt_s = socket.socket(type=socket.SOCK_DGRAM)
    ip_port = ('localhost', 8091)
    skt_s.bind(ip_port)
    ret, addr = skt_s.recvfrom(1024)
    print(ret.decode('utf-8'))
    skt_s.sendto(ret, addr)
    skt_s.close()


if __name__ == '__main__':
    # place_tcp()
    place_udp()