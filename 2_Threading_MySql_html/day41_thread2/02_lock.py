"""线程锁
    多线程中,仍然需要锁

    死锁: 互斥锁产生的现象

    递归锁/重入锁
        RLock: 可以被一个线程,多次获取, acquire和release可以嵌套.
                只有最外面release了,才能让其他线程继续处理acquire阻塞.
"""
import time
from threading import Lock, Thread, RLock

# noodle_lock = Lock()
# fork_lock = Lock()

noodle_lock = fork_lock = RLock()


def eat1(name):
    noodle_lock.acquire()
    print('%s拿到面条啦'%name)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    fork_lock.release()
    noodle_lock.release()
    # noodle_lock.release()  # 递归锁中, release一定是成对的. 如果release多了,会导致runtimeerror异常


def eat2(name):
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s拿到面条啦'%name)
    print('%s吃面' %name)
    noodle_lock.release()
    fork_lock.release()


Thread(target=eat1,args=('alex',)).start()
Thread(target=eat2,args=('Egon',)).start()
Thread(target=eat1,args=('bossjin',)).start()
Thread(target=eat2,args=('nezha',)).start()