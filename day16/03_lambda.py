"""
匿名函数lambda
1.结构
    ---- lambda 函数参数:内部逻辑
    ---- 参数可以有多个，用逗号隔开，与正常函数一致

2.常与max min sorted filter map一起用

3.例子

# 以字典的value进行排序，得出value最大的那个key
dic = {'k1':30,'k2':42,'k3':1}
print(max(dic, key=lambda key:dic[key]))

# 现有两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# tup1 = (('a'),('b'))
# tup2 = (('c'),('d'))

tup1 = (('a'),('b'))
tup2 = (('c'),('d'))
print(list(zip(tup1, tup2)))
g = lambda x,y:[{x:y}for x,y in zip(tup1, tup2)]
print(g(tup1, tup2))

"""

# sqrt = lambda x,n:x*n
# print(sqrt(10,5))

# 转换为匿名函数
# def plus(x,y):
#     return x+y

# plus = lambda x,y:x+y
# print(plus(3,5))

# 以字典的value进行排序，得出value最大的那个key
# dic = {'k1':30,'k2':42,'k3':1}
# print(max(dic,key=lambda key:dic[key]))

# 对列表的每个元素求平方
# l = [1,2,3,4,5,6,7]
# print(list(map(lambda x:x*x,l)))

# 筛选列表中大于4的数
# a = filter(lambda x:x>4,l)
# print(list(a))

# 现有两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# tup1 = (('a'),('b'))
# tup2 = (('c'),('d'))
# zzz = lambda a,b:[{i:j} for i,j in zip(a,b)]
# print(zzz(tup1,tup2))

# print(list(map(lambda t:{t[0]:t[1]},zip(tup1,tup2))))

# print([{i:j} for i,j in zip(tup1,tup2)])
