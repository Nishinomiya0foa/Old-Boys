# 协程  ---- 在一个线程上 提高cpu的利用率
    # 本质上是一个线程.
    # 能够在多个任务间切换来节省IO时间  ----遇到IO操作就切换到其他任务
    # 协程间任务切换的时间开销,远小于进程或线程间的切换时间


# 使用greenlet模块完成的切换
import greenlet
import gevent


# def eat():
#     print('Eating start.')
#     g2.switch()
#     print('Eating end.')
#     g2.switch()
#
# def play():
#     print('Playing start.')
#     g1.switch()
#     print('Playing end.')


# g1 = greenlet.greenlet(eat)
# g2 = greenlet.greenlet(play)
# g1.switch()


# gevent
#   g1 = gevent.spawn(func, 1,2,3)  创建一个协程, 参数为1,2,3


import gevent
import time
from gevent import monkey;monkey.patch_all()  # 会把之后模块中的阻塞操作打包,可以识别

def eat():
    print('Eating start.')
    time.sleep(3)
    print('Eating end.')


def play():
    print('Playing start.')
    time.sleep(1)
    print('Playing end.')


g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

g1.join()  # 等待g1 g2完成
g2.join()

# 异步
from gevent import monkey;monkey.patch_all()
import time
import gevent

def task():
    time.sleep(1)
    print('zxc')


def asyn():
    g_list = []
    for i in range(10):
        g = gevent.spawn(task)
        g_list.append(g)
    gevent.joinall(g_list)  # 同时join
                            # [g.join() for g in g_list]

asyn()
