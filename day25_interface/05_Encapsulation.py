"""封装 Encapsulation  ---- 面向对象的思想本身就是一种封装
目的：保护代码

狭义上的封装，面向对象的三大特性之一
    把属性和方法隐藏
"""

# 创建了一个用户类
# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd
#
# my_user = User('陈', 123123)
# print(my_user.pwd)
# my_user.pwd = 1234
# print(my_user.pwd)

# 上面的那个类能从外部访问pwd,甚至修改。非常不安全
# 我需要把pwd属性设为私有，无法从外部访问
class User:
    __key = '123'  # 类中私有静态属性
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd  # self.__pwd 定义了一个私有属性pwd，无法外部访问

    def get_pwd(self):
        return self.__pwd  # 私有属性可以在类的内部被调用，调用时__pwd，需要双下划线

    def __get_name(self):  # 私有方法，供内部调用,外部无法访问
        return self.name[0]

    def pr_name(self):
        print(self.__get_name())

my_user = User('陈wen', 123123)
# print(my_user.pwd)  # 无法访问，会报错;不准访问
# print(my_user.__dict__)
print(my_user.get_pwd())
my_user.pr_name()

# 类中的私有属性或方法，都是在变量的所编加上双下划线 例如：self.__name = name
# 私有属性或方法，只能在类中调用
    # 对象的私有属性
    # 类中私有方法
    # 类中静态属性