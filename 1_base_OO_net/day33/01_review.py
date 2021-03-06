# 黏包问题的出现
    # TCP协议中才有黏包问题
    # TCP协议是面向流的协议，并且TCP协议中有缓存机制，Nagle算法来避免丢包
    # 这样就导致在发送连续小数据时，以及接受大小不符（skt.recv(length)）时，容易出现黏包现象

# 解决黏包问题
    # 定制报文，传输报文前，先发送报文长度。

# struct 模块
    # 作用：把python中的各数据类型转换为固定长度的bytes类型数据
    # 方法： pack，unpack
        # 模式： “i”， 指要转换的数据类型为int，会转换成4个字节
        # unpack之后拿到的是一个元组tuple，tuple(0)为解包的那个数据

