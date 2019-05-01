"""开启多进程的另一种方式:利用面向对象的思想
1.自定义类,继承Process类
2.类中实现run方法,run()中代码是子进程中要运行的程序.
"""
import os

from multiprocessing import Process


class MySubprocess(Process):
    def __init__(self,name,age):
        super().__init__()  # 调用父类的__init__方法,
        self.name = name
        self.age = age

    def run(self):  # 必须为run方法
        print(self.pid)  # 子进程的进程号
        print(os.getpid())  # 当前进程的进程号, 即子进程的进程号
        print('My name is {}, my age is {}.'.format(self.name, self.age))
        print(self.is_alive())


if __name__ == '__main__':
    p = MySubprocess('Chen', 24)
    p.start()


