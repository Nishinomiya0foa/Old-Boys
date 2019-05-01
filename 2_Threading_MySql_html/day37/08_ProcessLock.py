"""Python中的多进程锁:需从multiprocessing中导入Lock
        ---- 牺牲部分性能,避免进程间资源争夺,保护数据安全
lock = Lock()  # 实例化一个lock对象, 该对象需传入子进程运行的函数内部;
lock.acquire()  #
lock.release()
"""

import json
import time

from multiprocessing import Process, Lock


class TestLock(Process):
    def __init__(self, lock):
        super().__init__()
        self.lock = lock
    def run(self):
        self.lock.acquire()
        with open('ticket') as f1:
            dic = json.load(f1)
            if dic['ticket'] >= 1:
                dic['ticket'] -= 1
                time.sleep(0.2)
                print('我使用了一张ticket, 现在还剩余{}张.'.format(dic['ticket']))
            else:
                print('无票')
        with open('ticket', 'w') as f2:
            json.dump(dic, f2)
        self.lock.release()



if __name__ == '__main__':
    lock = Lock()
    for i in range(5):
        p = TestLock(lock)
        p.start()