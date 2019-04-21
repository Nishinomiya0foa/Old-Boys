# 狗类  ---- 吃 喝 看门
# 鸟类  ---- 吃 喝 下蛋

class Animal():  # 父类中定义了共有的属性和方法
    def __init__(self, name):
        self.name = name

    def eat(self):  # 都拥有eat()方法
        print('{} can eat.'.format(self.name))

class Dog(Animal):
    def lookdoor(self):
        print('only {} can lookdoor.'.format(self.name))

# class Bird(Animal):
#     def downegg(self):
#         print('only {} can downegg.'.format(self.name))

febby = Dog('菲比')
febby.eat()
febby.lookdoor()

# 这样会有一个问题。 如果子类中也要有__init__()，和新的属性。应该怎么做呢？
class Bird(Animal):
    def __init__(self,name, gender):  # 参数为子类的全部参数
        # Animal.__init__(self,name)  # 调用父类的__init__方法，把self（这里的self是创建Bird类时创建的self），
                                    # 以及父类需要的参数传入； 这就是派生
        super().__init__(name)  # 使用super关键字，能同样完成派生属性的功能。不同的是不用传self，和父类名字
                                # 不用传参。
                                # 只在python3中有
        self.gender = gender  # 派生属性

    def downegg(self):  # 子类的派生方法
        print('only {} can downegg.'.format(self.name))

    def eat(self):  # 都拥有eat()方法
        # Animal.eat(self)  # 子类中想同时也调用父类的方法eat()。这种方式
        super().eat()   # 使用super调用父类方法名，不需传参数
        print('{}:\'emmmmm...\''.format(self.name))


kulu = Bird('kulu', 'MALE')
# print(kulu.name)
kulu.eat()
# super(Bird, kulu).eat()  # 参数为类和他的实例，返回父类的方法
                        # 可在外部使用，需进行传参

"""派生：在父类属性之外，新增加了属性或方法
有派生属性和派生方法
进行调用时，优先调用子类作用域中对象，然后才是父类中的
如果想同时调用子类和父类的同一方法，需在子类方法中先调用了父类方法。
"""