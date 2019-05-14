"""守护线程
    与守护进程不同的是:
        守护线程会随着主线程的结束而结束, 而主线程会在其他子线程全部结束之后才会结束.
    ---- 这是因为主线程结束后,整体资源都会回收,其余子进程无法独立运行.

    join() 同步线程
"""
import time
from threading import Thread


def func1():
    print('22222')
    time.sleep(10)
    print('222222222222222222222222')


def func2():
    print('11111111111111')
    time.sleep(5)


if __name__ == '__main__':
    t = Thread(target=func1)
    t.daemon = True  # 设置了守护线程, 主线程结束后, 守护线程直接结束
    t.start()

    t2 = Thread(target=func2)
    t2.start()

    t.join()
    t2.join()
    print('主线程')