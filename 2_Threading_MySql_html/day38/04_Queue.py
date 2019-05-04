"""队列: 先进先出
    ---- 这里用于进程间的通信(简写:IPC)

q = Queue(5)  # 实例化一个队列, size=5
q.put('string')  # 往队列里存内容,当超出最大容量时,阻塞直至队列不满时
q.get(block=True , timeout=3)  # 从队列中取一个值,当队列已经为空时,阻塞直至队列不为空时
                                # block默认为True,表示无值时阻塞;timeout默认为0,表示超出这个时间,没有值,报异常
q.full()  # 队列是否满了, 当有多进程同时访问这个队列时, 状态可能不准确.
q.empty()  # 队列是否为空

q.get_nowait()  # 不等待,直接取值;无值时报异常
"""

from multiprocessing import Queue, Process


class Produce(Process):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        self.q.put('Hello!')


class Consume(Process):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        print(self.q.get())


if __name__ == '__main__':
    q = Queue(5)
    p = Produce(q)
    p.start()

    c = Consume(q)
    c.start()

