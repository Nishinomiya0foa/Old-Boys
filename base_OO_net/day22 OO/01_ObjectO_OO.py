"""OO:面向对象  ---- 适合复杂的程序
优点：易于扩展
缺点：可控性差

类：抽象
对象、实例：具体存在。  先有类，再有对象

类可以规范对象
"""


# 基本结构
class Person:  # Person类名：操作属性，查看属性  ---- 类名
    country = 'China'   # 创造类中全局属性,类属性，即静态属性，静态属性无法在外部更改；所有实例对象都拥有这个属性

    def __init__(self, *args):  # 调用这个类时，会自动调用__init__()方法；self是一个必须传递的参数  ---- 初始化方法
                                                                        #                           ---- self是对象，必须传
        # 可以把self看做系统赠送免费使用的大字典，只能类里面用，接收和传递参数
        self.name = args[0]  # name -- 属性； 把args[0]的值赋值给name
        self.age = args[1]

    def walk(self,n):       # ---- 方法，一般情况下，必须传self参数，self必须为第一个。之后可以传其他参数
        print('{}走啊。再走{}步'.format(self.name, n))
    aaa = 'aa'


chen = Person('chenwb', 23)  # 实例化。 类名用来实例化。
zhang = Person('zhangl', 23)
print(chen.name)  # 返回 name 属性
print(zhang.country)    # 实例也有类中静态属性。
chen.walk(5)  # 调用实例的方法，同时传递了self；等同于 Person.walk(chen)
print(Person.country)   # ---- 类名可以查看静态属性，不需实例化
# zhang.walk(3)
chen.name = 'cwb'   # 修改对象属性
# del chen.name # 删除对象属性
print(chen.__dict__)


# 对象 = 类名(*args)  -》 实例化
# 类名()会创建一个对象，
# 调用__init__()方法。类名(*args)的参数会被这儿接收
# 执行__init__()方法
# 返回self


# 对象能做的事：
    # 查看属性
    # 调用方法
# 类名能做的事
    # 实例化
    # 调用方法  ---- 不过这一般是对象做的事
    # 调用类中的属性，即调用静态属性
    # 静态属性不能修改





