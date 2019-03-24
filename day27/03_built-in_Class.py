"""类的内置方法 双下划线"""

# __str__      str(obj)
# __repr__    repr(obj)
    #    获取原类型的格式

class Teacher:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Teacher\'s object:{}'.format(self.name)

    def __repr__(self):
        return str(self.__dict__)

a = Teacher('小陈', '23')
# print(a)  # 打印一个对象的时候，就是调用object类中的a.__str__
#             # 我在类中重写了__str__方法，所以会优先调用我写的方法.为了更有好，我重写了

print(repr(a))  # __repr__是__str__的备胎 -》如果没有__str__，则会调__repr__
# 当print() / '%s' % obj / str(obj)时，实际上是内部调用了obj.__str__方法，如果有str方法，返回字符串
# 如果没有__str__，则返回obj.__repr__的返回值，如果没有，会在父类中重复这个寻找顺序

# __len__  不是所有对象都拥有len()方法
# print(len(a))  # a就没有len()方法
class Classes:
    def __init__(self, name, student_nums):
        self.name = name
        self.student = student_nums

    def __len__(self):
        return self.student

    def __del__(self):
        print('Classes 方法删除了')

chuer = Classes('初二2班', 45)
print(len(chuer))


# 析构函数 __del__  就是平时说的删除，从内存中回收
# 在删除一个对象之前，进行一些收尾工作
class A:
    def __del__(self):
        print('执行呢')

b = A()
# del b  # 即使我重写了del方法，析构的功能也被执行了，这里的重写更像补充
        # 当调用del方法时，既执行了删除，又执行了我重写的方法
        # 即使我没有调用del方法， 在程序执行完成时，也会自动调用del方法


# __call__
# 一个实例 加上()  相当于执行__call__方法。 例如： a = A()  a()
class B:
    # def __init__(self, name):
    #     self.name = name

    def __call__(self, *args, **kwargs):
        # print('{}, 我在这儿了'.format(self.name))
        print('here!!!!!')
# bb = B('小陈')
bb = B()()
# bb()



