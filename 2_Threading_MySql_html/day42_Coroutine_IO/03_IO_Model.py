# 复习
#     同步: 提交任务之后,需等待任务执行完毕
#     异步: 提交任务后,不进行任何等待操作
#     阻塞: 程序遇到recv recvfrom accept等, 程序暂停运行
#     非阻塞:


"""IO 模型
    两段阻塞: 1. 等待数据准备
            2. 将数据从内核拷贝到进程
blocking IO: 阻塞IO
nonblocking IO: 非阻塞IO  ---- 不阻塞, 但会一直循环调用,不推荐使用.
multiplexing IO: 多路复用IO  ---- 优势在于处理多个连接
"""

while True:
    print('1')

