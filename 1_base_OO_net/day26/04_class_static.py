"""
staticmethod  静态方法
    一个方法不想和他的类没有任何数据交互，只单纯被外部调用，这个方法就可以被 staticmethod 变成静态方法
    静态方法需要进行 @staticmethod 装饰
    调用过程就像最普通的函数，只是前面带了一个类名. 而已

classmethod  类方法
    当类中有个方法的操作只涉及静态属性时，就应该使用classmethod来装饰。之后可以直接被类调用
    定义的方法有一个默认参数 cls， 代表当前类

类方法和静态方法都是通过类去调用的。
也可以通过实例调用，但最好是类调用

"""

# 想把discount设为私有静态属性，那么怎么在外部改变这个值呢？
# 例子: 类方法
class Goods:
    __discount = 0.6
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod  # 声明类方法， 这个类方法只使用了类中的静态属性。 self.__discount
    def change_discount(cls, new_discount):  # 参数cls是默认参数，指代这个类
        Goods.__discount = new_discount

apple = Goods('苹果', 5000)
print(apple.price)  # 默认6折 所以这儿打印的结果应该是3000

# 类方法被类调用，不依托对象调用
Goods.change_discount(0.5)  # 调用定义的类方法 change_discount，传参数0.5
                            # 然后执行change_discount()方法。
print(apple.price)

