"""抽象类
如果说 类 是从一堆 对象 中抽取相同的内容而来的，那么，
    抽象类 就是从一堆 类 中抽取了相同的内容。
Python中抽象类与接口类的区别：
    1.实际上没有区别。
    2.人工分出来的区别：
        1.一般情况下，抽象类都是单继承；而接口类默认多继承
        2.抽象类中可以实现方法（实现的方法可以通过super调用)；接口类不准
时刻记住：抽象类和接口类都是规范！
"""
# 抽象类 也是 规范
# 一般情况下，抽象类都是单继承。 能实现的功能都是非常相似的
# 单继承比较简单，所有容易抽象出相同功能实现在父类中
# 多继承的情况，由于功能比较复杂，所以不容易抽象出相同的功能实现在父类中

from abc import abstractmethod, ABCMeta
class File(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        print('I can do read.')

    @abstractmethod
    def write(self):
        print('I can do write.')

class Txt(File):
    def read(self):
        # super().read()
        print('Txt can do read.')

    def write(self):
        print('Txt can do write.')

t = Txt()
t.read()

