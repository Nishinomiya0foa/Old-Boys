"""继承:继承是一种创建新类的方式。新建的类可以继承一个或多个父类。这个新建的类称为子类
增加代码复用性。
子类 是 父类。 父类包含子类。
"""

# 正常情况定义一个简单的类：
class A(object):pass

# 再定义另外一个简单的类：
class B:pass

# 定义A类的子类
class A_Son(A):pass  # A是父类，也叫超类、基类；A_Son为子类，也叫派生类

# 一个类可以被多个类继承
class A_Son1(A):pass

# 一个类可以继承多个父类 ----多继承
class AB_Son(A,B):pass # A,B都是父类，同时继承AB

print(AB_Son.__bases__)  # 查看父类
print(A.__bases__)  # python3中，所有的类都默认继承 object类  --- 新式类