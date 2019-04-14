"""TCP和UDP协议"""

# 通过端口访问各个程序
    # 每一个需要网络通信的程序，有会开一个端口
    # 同一时间，一个端口只会被一个程序占用
    # 端口的范围： 0-65535
    # 自己开的端口，一般在 8000之后

# ip  ---- 确定唯一的一台机器
# ip+端口 ---- 确定这台机器上的一个程序

"""TCP协议：可靠安全，面向连接的，超时重发
            ---- 当建立通信之后会一直占用网络连接，不会断开，除非申请断开
三次握手：建立全双工通信
    ---- 全双工： 双发都可以收发信息
数据传输：当server收到信息时，会返回一个序列号告知client收到了信息
四次挥手：结束通信
    结束比建立多一次的原因：当server端收到FIN请求时，很可能并不会立即关闭SOCKET，所以只能先回复一次ACK，告知CLIENT，成功接收；
                            当确认server端报文全部发送之后，再发送一次FIN请求。所以这一步需要分为两步
"""

"""UDP 协议
1.收到信息不需要对方确认，比较快，但不安全
2.不会一直占用连接
"""

# 应用层
# 传输层：TCP/UDP协议
# 网络层：ip协议
# 数据链路层：srp协议
# 物理层



# 画三次握手 四次挥手
# 画互联网协议过程