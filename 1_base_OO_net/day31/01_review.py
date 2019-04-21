# import logging
#
# logger = logging.getLogger()
#
# formatter_1 = logging.Formatter('%(filename)s - %(levelname)s - %(lineno)s')
# formatter_2 = logging.Formatter('%(filename)s - %(levelname)s - 行数：%(lineno)s')
#
# fh = logging.FileHandler('test.log', 'a', encoding='utf-8')
# sh = logging.StreamHandler()
#
# fh.setFormatter(formatter_1)
# sh.setFormatter(formatter_2)
#
# logger.setLevel(logging.DEBUG)
# fh.setLevel(logging.ERROR)
# sh.setLevel(logging.NOTSET)
#
# logger.addHandler(fh)
# logger.addHandler(sh)
#
# logger.error('ERROR!')
# logger.debug('DEBUG!')

# encode()  转bytes类型
# decode（'utf-8'） 转其他类型

# MAC地址
# ARP协议：通过ip找mac（广播）
# IP地址：一台机器在网络上的位置
# 公网IP, 局域网IP
# 端口号：有网络通信需求的程序会申请一个端口，同一个端口同一时间只能被一个程序占用
    # 一般自己申请的端口号都要求是：8000之后的

# TCP UDP 协议
    # TCP：全双工，可靠（数据不易丢失），面向连接，慢
        # 三次握手和四次挥手
        # 长连接：同时只能与一个client对象建立通信
    # UDP：不可靠，无连接，快

# IP协议属性网络osi七层协议中的哪一层？   网络层
# TCP协议和UDP协议属于哪一层？   传输层
# ARP协议属于？  数据链路层