"""基于udp的socket"""

# 不需要监听，不需要建立连接
# 在启动服务之后只能被动等待客户端发送消息

# 客户端发送消息时会自带地址信息
# 回复客户端消息时，需要填写对方的地址

print('\033[0;32;0m这是一条test信息\033[0m')

import time
t_format = '%H:%M:%S'

t = time.time()
timeArray = time.localtime(t)
t_msg = time.strftime(t_format, timeArray)

t_msg = t_msg.encode('utf-8')
print(t_msg)
t_msg = t_msg.decode('utf-8')
print(t_msg)