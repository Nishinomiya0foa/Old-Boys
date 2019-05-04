import socket
from multiprocessing import Pool

def chat(conn, addr):
    conn.send('Hello'.encode('utf-8'))
    msg = conn.recv(1024).decode('utf-8')
    print(addr[1], msg)



if __name__ == '__main__':
    ip_port = ('', 8338)

    skt_s = socket.socket()

    skt_s.bind(ip_port)

    skt_s.listen()  # 监听

    while True:
        conn, addr = skt_s.accept()
        p = Pool(4)
        p.apply_async(func=chat, args=(conn, addr))
    conn.close()
    skt_s.close()
