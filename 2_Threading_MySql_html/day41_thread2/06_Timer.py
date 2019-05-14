"""Timer 定时器
    Timer类是 Thread类的子类
    Timer(time, func)   定时开启线程, time秒之后,开启线程
                        非阻塞

    t.cancel() 取消定时器和他之后执行的函数.
"""
import time
from threading import Timer

def func():
    print('时间同步')

while True:
    t = Timer(5, func)
    t.start()
    time.sleep(3)
    t.cancel()

