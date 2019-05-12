"""线程 ---- cpu调度的最小单位
    概念：
    1. 轻型实体： 线程中的实体基本上不拥有系统资源，只需能保证独立运行的资源
                    包括程序，数据和TCB。 线程是动态概念，它的动态特性由线程控制块TCB描述。
    2. 可并发

进程和线程的区别：
    1.地址空间和其他资源（文件、代码），在进程间相互独立；同一进程的各线程间共享。
    4.在多线程操作系统中，进程不是一个可执行的实体。

Cpython 解释器的特性. Jpython解释器则没有
全局解释器锁 GIL  ---- 为了数据安全,同一时刻只能有一个线程访问cpu,降低了cpu效率
    锁的是线程

"""

import time
import os
from threading import Thread, current_thread, active_count, enumerate, main_thread
                      # 线程      当前线程     活跃线程数   活跃线程列表  主线程
print(current_thread())  # 当前线程名,线程id


def func(n):
    time.sleep(1)
    global g  # 方法内使用全局变量
    g = '滚'
    print(n, current_thread(), active_count())  # 在同一个进程里
    print(enumerate())


if __name__ == '__main__':
    g = 'Hello'
    t_list = []
    print(os.getpid())
    for i in range(5):  # 并发
        thr = Thread(target=func, args=(i,))
        thr.start()
        t_list.append(thr)
    print('主线程:', main_thread())
    print(active_count())
    [t.join() for t in t_list]
    print(g)
    # 也可以通过类继承的方式来实现多线程
