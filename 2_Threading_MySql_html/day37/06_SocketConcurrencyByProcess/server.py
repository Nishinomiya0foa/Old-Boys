from socket import socket
from multiprocessing import Process


class ConnTcp(Process):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):  # 子进程中需执行的函数
        ret = self.conn.send('你好'.encode('utf-8'))
        msg = self.conn.recv(1024).decode('utf-8')
        print(msg)
        self.conn.close()


if __name__ == '__main__':
    skt_s = socket()
    ip_port = ('', 8091)
    skt_s.bind(ip_port)
    skt_s.listen(5)
    while True:
        conn, addr = skt_s.accept()  #
        p = ConnTcp(conn)  # 每次有accept到conn,addr开启一个子进程
        p.start()

