from socketserver import (StreamRequestHandler as SRH, TCPServer as TCP)

ip_port = ('', 8091)


class MyTCPServerHandler(SRH):
    def handle(self):
        msg = self.request.recv(1024).decode('utf-8')
        msg = msg.upper()
        print(msg)


tcp_server = TCP(ip_port, MyTCPServerHandler)
tcp_server.serve_forever()