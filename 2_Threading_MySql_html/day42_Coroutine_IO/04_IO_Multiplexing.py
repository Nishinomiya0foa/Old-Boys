"""multiplexing IO:
            IO 多路复用
        ---- windows中使用select模块
                selectors模块更好用, 可根据操作系统选择最合适的多路复用模型.
        ---- linux使用 poll模块     轮询机制(循环列表)
                       epoll模块      更好
            """

