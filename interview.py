# 生成器 打印出的值是什么
# def demo():
#     for i in range(4):
#         yield i
# g=demo()  # g接收yield 的所有值
# g1=(i for i in g)  # 生成器
# g2=(i for i in g1)  # 生成器
# print(list(g1))  # [0,1,2,3]
# print(list(g2))  # [] 这是因为生成器生成的值都会取完了。所有g2中的值是空的



# def add(n,i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g=test()
# for n in [1,10, 5]:  # n为1或10
#     """由于未调用时，生成器表达式不会执行。拆开来看"""
#     g=(add(n,i) for i in g)  # g = (add(n,i) for i in
# print(list(g))


# l = list(range(10))
# n = l.copy
# print(n)

"""判断字典有没有某个key的方法"""
# dic = {'b':1}  # 用get可能会有问题
# if 'x' in dic:
#     print(True)

"""以下代码输出什么"""
# def extengList(val, list=[]):
#     list.append(val)
#     return list
# list1 = extengList(10)
# list2 = extengList(123,[])
# list3 = extengList('a')
# print(list1)
# print(list2)
# print(list3)

# print(True or False and True)

"""
is 和 == 的区别：
unicode utf-8 gbk编码之间的关系：
"""

"""算法实现删除list中重复元素"""
# lis = [1,1,3,3,24,5623,12,31,1,3]
# lis2 = []
# for i in lis:
#     if i not in lis2:
#         lis2.append(i)
# lis = lis2
# print(lis)