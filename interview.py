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
for n in [1,10,5]:  # n为1或10
    g=(add(n,i) for i in g)  # g = (add(n,i) for i in

# n = 1
# g = (add(n,i) for i in g)
# n = 10
# g=(add(n,i) for i in (add(n,i) for i in (0,1,2,3)))  # 可以装化为这种形式
# g = (add(n,i) for i in (10, 11, 12, 13))
# g = (20, 21, 22, 23)

# 如果 for n in [1,10,5]
#n = 10 时
g=(add(n,i) for i in (add(n,i) for i in g))
# n = 5 时
g = (add(n,i) for i in (add(n,i) for i in (add(n,i) for i in (0,1,2,3))))



print(list(g))

#    1，0 /1/2/3
#     1  2  3  4


