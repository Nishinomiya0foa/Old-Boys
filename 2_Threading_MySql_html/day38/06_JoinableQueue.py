"""JoinableQueue:
    ---- 相比于Queue,每一次get了值,需提交一次回执(q.task_done())
            q.join()  # 阻塞 知道一个队列中的所有数据,全部被处理完毕

在消费者:
    1.每次获取一个数据
    2.处理这个数据
    3.发送一个标识: 成功处理数据

生产者:
    1.每次生产一个数据
    2.将这个数据放入队列
    3.在队列中刻上一个记号
    4.全部生产完毕, 发出join()信号; 等待之前刻上的记号都被消费者处理完,join()阻塞结束
"""
import random
import time
from multiprocessing import Process, JoinableQueue


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
        self.q.join()


class Consumer(Process):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q

    def run(self):
        while True:
            time.sleep(random.randint(1, 3))
            print('\033[31m{}消费了{}\033[0m'.format(self.name, self.q.get()))
            self.q.task_done()

if __name__ == '__main__':
    q = JoinableQueue(11)
    p1 = Producer('小陈', '包子', q)
    p2 = Producer('周扒皮', '土', q)
    p1.start()
    p2.start()

    c1 = Consumer('阿雷', q)
    c2 = Consumer('小张', q)
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()