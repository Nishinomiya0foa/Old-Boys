"""面向对象进阶"""

# __getitem__
# __setitem__
# __delitem__

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 可以通过类似字典键值的方式来取属性； f['xx']
    def __getitem__(self, item):  # 如果没有item相关的方法，则通过 f.xx 来取值
        if hasattr(self, item):
            return self.__dict__[item]

    # 可以通过类似字典键值对的方式来 传值。  f['xx'] = obj
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    # 也可以使用类似的方式来进行删除
    def __delitem__(self, key):  # 接收一个参数
        del self.__dict__[key]


f = Foo('Chen', 34)
print(f['name'])  # 在类中通过类似键值队的方式来取值
f['hobby'] = 'game'  # 添加了一个属性并赋值
print(f.hobby)
print(f.__dict__)
del f['hobby']
print(f.__dict__)

# __new__  构造一个对象，几乎用不到；但面试时可能会被考
# 单例模式  ---- 设计模式的一种，当第一次实例化时，创建一个实例化对象
         #  ---- 再次实例化时， 使用之前创建的对象
        # ---- 一个类始终只有一个实例

# class A:
#     __instance = False
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):  # 一个构造方法
#         if cls.__instance:  # 如果没有实例
#             return cls.__instance  # 实例化时创建
#         cls.__instance = object.__new__(cls)  # 有新的实例则覆盖掉老的
#         return cls.__instance

# chen = A('chen',23)
# bibi = A('BIBI', 24)
# print(chen, bibi)
# print(chen.name)  # 会被覆盖
# print(bibi.name)

# __eq__ 可以更改判断== 的方式为判断值。 否则为判断内存地址
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # 在进行 == 判断时，会执行这个函数
#     def __eq__(self, other):  # 如果两个实例的属性值相等，就相等
#         return True if self.__dict__ == other.__dict__ else False
# a = A('chen', 23)
# b = A('chen', 23)
#
# print(a==b)  # 如果没有 __eq__ 方法。 则判断内存地址，有则执行__eq__方法

# __hash__  哈希
# 使得属性值相同时，哈希地址能相同
# set 依赖对象的hash 和 eq
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name+self.age)

    def __eq__(self, other):
        if self.__dict__ == other.__dict__:
            return True
        return False

a = A('chen', '23')
b = A('chen', '23')
print(hash(a), hash(b))
print(set((a,b)))  # 依赖内置函数 __hash__ 和 __eq__