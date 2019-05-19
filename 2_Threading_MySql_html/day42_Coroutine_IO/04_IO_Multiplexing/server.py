"""多用复用io 模型"""

import select
import socket

skt_s = socket.socket()
ip_port = ('', 8091)
skt_s.setblocking(False)
skt_s.bind(ip_port)
skt_s.listen(1)

read_lst = [skt_s]
while True:
    r_list, w_list, x_list = select.select(read_lst,[],[])

    for i in r_list:
        if i is skt_s:
            conn, addr = i.accept()
            read_lst.append(conn)
        else:
            ret = i.recv(1024)
            if ret == b'':
                i.close()
                read_lst.remove(i)
                continue
            print(ret)
            i.send(b'Gun!')