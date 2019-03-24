"""接口类的多继承"""
# 什么时候用多继承？

# 有一个动物园
# 要实现3个类。tiger。swan(天鹅)，eagle
# 分别有以下方法
# tiger: walk,swim
# swan: walk,swim,fly
# eagle: walk,fly
# 如果分别定义这个三个类，把他们的各自方法依次实现，代码重复量过多，可读性差
# 我想尽量少的定义：
# class Animal:
#     def walk(self):pass
#     def swim(self):pass
#     def fly(self):pass
# tiger = Animal()  # 可是tiger不应该有fly方法。失败

# 于是我换了一个思路
from abc import abstractmethod, ABCMeta

class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):pass
class SwimAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):pass
class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):pass

class Tiger(WalkAnimal,SwimAnimal): # 我上面规范了WalkAnimal类中必须有的方法，这里的子类中也必须实现规范的方法。否则报错
                                    # TypeError: Can't instantiate abstract class Tiger with abstract methods walk
    def swim(self):                 # 以上报错的意思是我没有重写规范中要求的walk方法
        pass
class Swan(WalkAnimal,SwimAnimal,FlyAnimal):pass
class Eagle(WalkAnimal,FlyAnimal):pass
# 这样我定义了几个类，后面想实现各个方法时，随便继承就OK了。
t = Tiger()

# 接口类满足接口隔离原则
# 接口隔离原则:使用多个专门的接口，而不使用单一的总接口。即客户端不应该依赖那些不需要的接口
# 按照上面的例子来讲，就是说：我要使用的是WalkAnimal，SwimAnimal等这些专门的接口，而不是笼统的Animal总接口。
