"""反射:用字符串类型的名字去操作变量"""

# isinstance(obj, cls)  # 判断obj对象是否为cls类的对象
# issubclass(cls_sub, cls_super)  # 判断cls_sub类是否为cls_super类的子类

# 反射对象中的属性和方法
# hasattr   ---- if hasattr(obj, str): 判断obj中是否有 str名字的对象
# getattr   ---- 获取
# setattr   ---- 修改变量
    # 不是很重要
    # setattr(cls, obj, str)  # 把cls类中的obj属性修改为str,obj不存在则新增obj属性。这个逻辑与正常的修改是一样的
# delattr  ---- 删除
    # 不太常用
"""面向对象中"""
class A:
    price = 20
    def func(self):
        print('I\'m func')

    @classmethod
    def pr_func(cls):
        print(A.price)

a = A()
a.name = 'alex'
# 反射对象的属性
ret = getattr(a, 'name')  # 通过变量名的字符串形式取到了值，第二个参数一定是字符串类型，这也是反射的目的
                        # 可以这样理解。   a.name = 'alex'
                        # 在进行反射时，getattr(obj, name),  obj就是类a，  name就是a中的属性name
print(ret)

# 反射对象的方法
if hasattr(a, 'func'):
    ret_func = getattr(a, 'func')  # 这个取到的是方法名！  需要加()才能执行方法
    ret_func()

# 反射类属性
print(getattr(A, 'price'))  # 与对象属性类似，只是把对象名换成了雷鸣

# 反射类方法： classmethod staticmethod
if hasattr(A, 'pr_func'):  # 判断是否存在这个方法，用法与getattr()一致
    getattr(A, 'pr_func')()  # 与反射对象的方法类似。同样是把对象名换成了类名

"""在模块中"""
from day27 import my_module
print(my_module.day)
# 取模块中的属性
print(getattr(my_module, 'day'))  # 取模块中的属性，用法一样
# 取模块中的函数
getattr(my_module, 'fn')()  # 用法都一样

year = '反射自身模块中的属性'
import sys
# print(sys.modules[__name__].year)  # sys.modules[__name__] 这一串就是当前模块

# 反射自身模块中的属性和方法
def test_f():
    print('反射自身模块中的方法')

getattr(sys.modules['__main__'], 'test_f')()  # 反射自身模块中的方法
print(getattr(sys.modules[__name__], 'year'))

# 可以反射内置模块
import time
print(getattr(time, 'time')())
print(getattr(time, 'strftime')('%m-%d %H:%M:%S'))  # 括号内正常传参


# 反射获取模块中的类
c = getattr(my_module, 'C')()  # 我反射得到了C， 并对他进行了实例化
print(c.__dict__)