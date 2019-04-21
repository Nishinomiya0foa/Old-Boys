import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        ret = self.request.recv(1024).decode('utf-8')
        print('{} : {}'.format(self.client_address[0], ret))

        self.request.send(ret.upper().encode('utf-8'))



if __name__ == '__main__':
    skts = socketserver.ThreadingTCPServer(('localhost', 8808), MyServer)
    skts.serve_forever()
