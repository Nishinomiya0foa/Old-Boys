# 时间同步
# 获取server端的时间

# 接收时间格式
# 将我的时间进行该格式的格式化。
# 发回客户端

import socket
import time

server_skt = socket.socket(type=socket.SOCK_DGRAM)

this_ip_port = ('127.0.0.1', 8080)

server_skt.bind(this_ip_port)

# 设置标志位，用来结束程序
flag = 0

while True:
    # 接收传来的格式信息
    t_format, addr = server_skt.recvfrom(1024)
    t_format = t_format.decode('utf-8')
    # 将本地时间按照传来的格式进行格式化
    t = time.time()
    timeArray = time.localtime(t)
    t_msg = time.strftime(t_format, timeArray)
    # 转为bytes类型
    t_msg = t_msg.encode('utf-8')

    # 发送t_msg
    server_skt.sendto(t_msg, addr)

    flag += 1
    if flag == 10:
        break

server_skt.close()
