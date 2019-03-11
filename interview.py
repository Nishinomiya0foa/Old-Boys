# 生成器 打印出的值是什么
# def demo():
#     for i in range(4):
#         yield i
# g=demo()  # g接收yield 的所有值
# g1=(i for i in g)  # 生成器
# g2=(i for i in g1)  # 生成器
# print(list(g1))  # [0,1,2,3]
# print(list(g2))  # [] 这是因为生成器生成的值都会取完了。所有g2中的值是空的



def add(n,i):
    return n+i
def test():
    for i in range(4):
        yield i
g=test()
for n in [1,10, 5]:  # n为1或10
    """由于未调用时，生成器表达式不会执行。拆开来看"""
    g=(add(n,i) for i in g)  # g = (add(n,i) for i in

# n = 1
# g = (add(n,i) for i in g)
# n = 10
# g = (add(10, i) for i in (add(10,i) for i in (0, 1, 2, 3)))
#
# 10 11 12 13
# 20 21 22 23


# 如果 for n in [1,10,5]
# n = 1
# g = (add(n,i) for i in g)
# n = 10
# g = (add(10, i) for i in (add(10,i) for i in g))
# n = 5
# g = (add(5, i) for i in (add(5,i) for i in (add(n,i) for i in (0, 1, 2, 3))))
#
# 5 6 7 8
# 10 11 12 13
# 15 16




print(list(g))

#    1，0 /1/2/3
#     1  2  3  4


