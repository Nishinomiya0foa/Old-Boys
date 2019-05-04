"""
    基于管道实现生产者消费者模型

"""
from multiprocessing import Process, Pipe

class Producer(Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    def run(self):
        pass


class Consumer(Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    def run(self):
        pass


if __name__ == '__main__':
    cons, prod = Pipe()


