"""
struct 模块
    可以把一个个数据类型转换为固定长度的字节流数据类型

"""
# 我们在网络上传输的所有数据，都叫数据包。数据包里的所有数据，都叫报文
# 报文里 不止有 数据 IP地址 mac地址  端口号

# 所有的报文 都有报头
"""定制报文"""
    # 如传输文件的时候定制的报头
        # 文件名，大小，文件类型，存储的路径

head = {'filename':'test', 'filesize':409600, 'filetype':'txt', 'filepath':r'\user\bin'}

"""自定义协议
协议并不复杂，我自己也可以定制协议；
"""
# server                                      # client
# 先发报头的长度                               # recv 报头长度
# 再发报头                                     # 获取报头,从报头中解析出报文长度
# 报文                                        # recv报文

# import struct
#
# ret = struct.pack('i',2000)  # 'i' 指 要把一个数字转换为固定长度的bytes类型
# print(ret)
#
# ret2 = struct.unpack('i', b'\nP\x00\x00')
# print(ret2[0])
