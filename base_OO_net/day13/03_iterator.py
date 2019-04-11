"""迭代器"""

# l = []
# print(dir(l))  # 返回该数据类型的方法


"""
    所有可被for循环的数据类型，都拥有__iter__方法
    可迭代协议：所有拥有__iter__方法的数据类型，都可被迭代

"""
# print([].__iter__())
"""
    一个可迭代的数据类型，执行了__iter__方法后，返回值为迭代器
    迭代器协议：内部含有__next__方法和__iter__方法的就是迭代器
"""

"""
    可被for循环，意味着可迭代
    迭代器也可迭代
    for循环就是在使用迭代器
    
    判断对象是否可迭代，执行一个他的__iter__方法
"""

"""
    迭代器的好处：
    1.从容器类型中一个一个取值，会把所有值都取到。
    2.可以节省内存空间。
            当迭代到那个值时(__next__())，才把那个值放入内存。而不是一次把所有对象加载到内存
    
"""


# print(dir([]))
# print(dir([].__iter__()))

# print(set(dir([])) & set(dir([].__iter__())))
# print(set(dir([].__iter__())) - set(dir([])))  # 看一下迭代器相比可迭代的数据类型（列表），他的特有的方法
#
# print([2,1].__iter__().__length_hint__())  # __length_hint__() 元素个数

# l = [1,2,3]
# iterator = l.__iter__()  # iterator是一个迭代器。
# print(iterator.__next__())
# print(iterator.__next__())

"""迭代器的__next__方法 可以一个个取值"""


# 用 while 模拟for循环
# l = [1,2,3,4,5]
# iterator = l.__iter__()  # 创建迭代器
# while 1:
#     print(iterator.__next__())

