"""多进程的几个启动方法
    1. join 异步变同步
"""
import time
from multiprocessing import Process


def fun(*args):
    for i in args:
        print('*'*i)
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=fun, args=(1,2,3,4,5,6))
    p.start()
    p.join()  # 感知一个子进程的结束, 之后才执行后续的程序; 异步 -> 同步
                # 让父进程停留在join这句话
    print('运行完了.')  # 执行这儿的时候,程序一定还没有运行完, 因为子进程中程序执行时间很长