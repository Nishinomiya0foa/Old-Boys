"""多继承
平时尽量不用！ 应使用单继承
"""

# class A:
#     def func(self):
#         print('A')
#
# class B:
#     def func(self):
#         print('B')
#
# class C:
#     def func(self):
#         print('C')
#
# class D(A, B, C):
#     pass
#     # def func(self):
#     #     print('D')
#
# d = D()
# d.func()    # 如果D()中有 func方法，则调用其本身的
            # 如果D()中没有func方法，则调用A类中的，从左往右，顺序为（A,B,C）

"""钻石继承
A,B,C,D 四个类
# PS。-> 表示继承关系
B->A  C->A   D->B,C   

"""
class A:
    def func(self):print('A')

class B(A):
    pass
    # def func(self):print('B')

class C(A):
    def func(self):print('C')

class D(B, C):
    pass
    # def func(self):print('D')

d = D()
d.func()    # 如果D()中，有func方法，则调用本身的
            # 如果D()中，无func方法，则调用父类B()中的
            # 如果父类B()中，也无func方法；则调用D()的第二个父类C()中的  ---- 先找同级的！
"""广度优先！"""
            # 如果第二个父类C()中，也无func方法，则找第一个父类的父类方法

print(D.mro())  # mro()方法记录了继承顺序
# 就近原则
# 新式类的继承顺序：广度优先
# 经典类的继承顺序：深度优先

# super的本质：不是直接找父类，而是根据调用者的节点位置的广度优先