"""生产者消费者模型
    # 为了解决数据供需不平衡的问题
"""
import random
import time
from multiprocessing import Process, Queue


class Producer(Process):
    def __init__(self, name, food, q):
        super().__init__()
        self.name = name
        self.food = food
        self.q = q

    def run(self):
        for i in range(5):
            time.sleep(random.randint(1, 3))
            f = '{}生产了{}{}'.format(self.name, self.food, i)
            self.q.put(f)
            print(f)


class Consumer(Process):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q

    def run(self):
        while True:
            if not self.q.get():
                print('取到了None')
                break
            time.sleep(random.randint(1, 3))
            print('\033[31m{}消费了{}\033[0m'.format(self.name, self.q.get()))

if __name__ == '__main__':
    q = Queue(6)
    p1 = Producer('小陈', '包子', q)
    p2 = Producer('周扒皮', '土', q)
    p1.start()
    p2.start()

    c1 = Consumer('阿雷', q)
    c2 = Consumer('小张', q)
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    q.put(None)
    q.put(None)