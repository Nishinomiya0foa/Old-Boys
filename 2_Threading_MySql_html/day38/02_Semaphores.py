"""信号量:与锁的作用类似
    # 限制固定数量的进程 同时访问代码段
"""
import json
import time
import random
from multiprocessing import Process, Lock, Semaphore

class TrySemaphore(Process):
    def __init__(self, man, sam):
        super().__init__()
        self.man = man
        self.sam = sam

    def run(self):
        self.sam.acquire()
        print('{}拿到了一把钥匙'.format(self.man))
        time.sleep(random.randint(1,6))
        print('{}还钥匙了!'.format(self.man))
        self.sam.release()

# 进程锁
class TryLock(Process):
    def __init__(self, lock):
        super().__init__()
        self.lock = lock

    def run(self):
        self.lock.acquire()
        with open('VeiwerLog') as f1:
            dic_view = json.load(f1)  #需符合json格式化要求
            if dic_view['viewer_count'] > 0:
                print('删除了一次访客记录')
                dic_view['viewer_count'] -= 1
            else:
                print('访客记录已为零.')
        with open('VeiwerLog', 'w') as f2:
            json.dump(dic_view, f2)
        self.lock.release()
if __name__ == '__main__':
    # lock = Lock()
    # for i in range(6):
    #     time.sleep(0.2)
    #     p = TryLock(lock)
    #     p.start()
    sem = Semaphore(4)
    for i in range(20):
        p = TrySemaphore(i, sem)
        p.start()
