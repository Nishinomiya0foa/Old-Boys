# 导入多进程
import time
import os
from multiprocessing import Process


def func(*args):
    print('子进程:',os.getpid())
    print('我的父进程:',os.getppid())  # 查看父进程的端口号
    print(args[0])
    print(args[1])
    time.sleep(2)
    print(3333333)


if __name__ == '__main__':
    # 创建子进程对象
    p = Process(target=func, args=(123123123,'你们好'))  # 注册   创建进程对象p
                                                # args用来接收参数,以元组的形式传参

    # 启动子进程
    p.start()  # 在另一个进程中执行函数func;在本进程中却没有执行

    print('*'*10)  # 与上述的子进程异步f;这里是主进程
    print('主进程:',os.getpid())  # 查看当前进程 端口号
    print('主进程的父进程:',os.getppid())  # 查看当前进程的父进程的端口号,就是pycharm的进程号

"""进程的生命周期
        主进程:
        子进程: 执行完子进程中程序,结束进程
        开启了子进程的主进程: 1.如果主进程中程序执行时间长,则执行完自身程序后结束
                            2.如果子进程中程序执行时间长,主进程会在主进程执行完后,等待子进程执行完,之后主进程才结束

"""

