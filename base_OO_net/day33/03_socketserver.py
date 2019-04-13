"""socketserver:同时与多个客户端通信"""


# 基本读懂源码

import socketserver

class MyServer(socketserver.BaseRequestHandler):  # 必须继承这个类
    def handle(self):  # 必须重写handle方法
        print(self.request.recv(1024))  # self.request 相当于 socket中的conn,即 conn,addr = skt.accept()中的conn
        self.request.send(b'123')
        print(self.client_address[0])  # 客户端的ip地址

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('localhost', 8080), MyServer)  # 线程thread  ---- 调度CPU的最小单位
    server.serve_forever()