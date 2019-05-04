"""
    管道: Pipe, 跨进程通信
        ---- 进程数据不安全: (recv的进程数量大于send时,可能出现), 用进程锁解决
"""

from multiprocessing import Pipe, Process


def func(conn1, conn2):
    conn2.close()
    while True:
        try:
            print(conn1.recv())
        except EOFError:     # 当管道内无数据,且管道两端其他连接都已经关闭时,仍进行recv(),抛出EOF异常.
            conn1.close()
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    Process(target=func, args=(conn1, conn2)).start()
    conn1.close()
    for i in range(10):
        conn2.send('Hello')
    conn2.close()