"""接口类、
是规范，是面向对象开发的思想。
"""

# 接口隔离原则:使用多个专门的接口，而不使用单一的总接口。即客户端不应该依赖那些不需要的接口

# 区别于抽象类
# 抽象类：python原生支持的
# 接口类：python原生不支持


# 开发一个支付
# 希望使用时感受不到分别调用wechat和alipay
class WeChat:
    def pay(self, money):
        print('使用wechat支付了{}元'.format(money))


class Alipay:
    def pay(self, money):
        print('使用Alipay支付了{}元'.format(money))

def pay(pay_obj, money):  # 统一支付入口 即归一化设计
    pay_obj.pay(money)


# 正常可以这样调用
wechat = WeChat()
# wechat.pay(100)
ali = Alipay()
# ali.pay(200)

# 但是我不想每次通过不同的对象去调用
# 只使用一个方法。  统一支付入口
pay(wechat, 200)
pay(ali, 10000)


# 但是如果新定义了一个类，applepay，里面没有实现pay方法，使用了其他命名，导致我统一的支付入口无法调用applepay；
# 我又该怎么做。
# 这个时候我可以定义一个规范类。 有方法名为pay，如果执行了这个pay方法，就报错
# 让多个支付类继承这个规范类，这样支付类中会重写pay方法。调用时就会调用子类的pay方法。正常执行
# 如果新定义的apple类，没有重写父类中定义的pay方法，那么后面调用时，就会抛出异常
# 格式如:
# class Payment():
#     def pay(self, name):
#         raise NotImplementedError  # 如果执行了这儿，主动抛出异常。这样开发中就会意识到我没有对pay函数进行重写。
#                                     # 后续需要继承这个Payment类

# 这样还有一个小问题，就是只有当我实例化调用了pay方法后，我才能依据异常发现有哪些子类不符合Payment的规范
# 以下类可以帮助我，这样在程序开发中只要实例化了子类，如果子类中没有pay方法，调用父类Payment中的pay方法时，就会直接抛出异常
# 并指出，缺少了pay方法
from abc import abstractmethod, ABCMeta  # 帮助建立规范的方法。可以对子类进行约束
class Payment(metaclass=ABCMeta):  # 指定元类：metaclass=ABCMeta 这个metaclass的定义就说明了这个类是规范类
    @abstractmethod  # 装饰器的调用。
    def pay(self, name):
        raise NotImplementedError
# 这个规范就是 接口类 或者 抽象类
# 接口类 默认多继承，接口类中所有方法都必须不能实现（没有具体代码实现）
# 抽象类 不支持多继承，抽象类中方法可以有代码实现