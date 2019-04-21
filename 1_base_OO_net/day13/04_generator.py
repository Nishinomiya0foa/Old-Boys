"""
生成器  ----本质也是迭代器:拥有__next__()和__iter__()方法

生成器函数
"""


# 生成器函数
# 含有yield关键字的函数都是生成器函数；yield不会结束函数
# yield关键字只能用在函数内部
# 不能与return共用
# yield的值返回给调用函数时
# def generator():
#     print(1)
#     yield 'a'
#     a = 2
#     yield 'c'
#
# # 生成器函数 执行后 返回生成器
# g = generator()  # g是一个生成器
#
# # 通过__next__()方法去访问每一个yield,及执行之前的代码
# print(g.__next__())
# print(g.__next__())


# 1000000个娃哈哈
# def generator_wahh():
#     for i in range(1000000):
#         yield '哇哈哈{}'.format(i)
#
# g = generator_wahh()
# g1 = generator_wahh()
#
# print(g, g1)
# for i in g:
#     print(i)

# 写一个生成器函数
def generator():
    for i in range(5):  # 由于for循环内部是yield，所以for循环不会一次循环完毕
        yield i

g = generator()
print(g.__next__())
for i in g:  # 会从上面__next__之后， 接着循环
    print(i)