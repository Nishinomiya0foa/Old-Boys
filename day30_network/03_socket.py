"""socket（套接字）
基于TCP的socket
socket：是应用层与TCP/IP协议族通信的中间软件抽象层，是一组接口

基于文件型：
基于网络型： AF_INET

# 有收必有发，收发数量等
"""

# 1.写一个自己和自己聊天的socket
# client 每10秒  time.time()把时间戳时间发给server
# server 接收时间戳时间，转换为格式化时间

import time

t = time.time()
t = str(t)
t = float(t)
timeArray = time.localtime(t)
s_t = time.strftime('%H:%M:%S', timeArray)

print(s_t)