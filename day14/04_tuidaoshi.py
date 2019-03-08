"""各种推导式：derivation"""
# 有列表的。地点的。生成器的。集合的
"""列表推导式"""
# 列表推导式:  [满足元素相关条件的元素或元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]
#               也可以没有if条件。那么会返回遍历了for循环的所有元素组成的列表
# 例如：
# print([x for x in range(10) if x % 2 == 0]) # 输出0-10中满足 x%2==0 的所有元素组成的列表

# 输出30以内所有能被3整除的数
# print([num for num in range(30) if num % 3 == 0])

# 输出30以内所有能被3整除的数的平方
# print([num ** 2 for num in range(30) if num % 3 == 0])

# 找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
# ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# print([i for lis in names for i in lis if i.count('e') > 1])  # 嵌套循环

# 效果等同于上面的列表推导式
# lis1 = []
# for lis in names:
#     for i in lis:
#         if i.count('e') > 1:
#             lis1.append(i)
# print(lis1)


"""字典推导式"""
# 将一个字典的key和value对调
# mcase = {'a': 10, 'b': 34}
# dic = {mcase[key]:key for key in mcase}  # 前面是原字典的value:原字典的key
# print(dic)

# 合并大小写对应的value值，将k统一成小写
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# dic = {key.lower():mcase[key]+mcase.get(key.upper(), 0)for key in mcase}
# print(dic)

"""集合推导式"""
# 和列表推导式一样。只是不允许有重复值
# sqt = {x**2 for x in [1,-1,2]} # 集合推导式
# sqt2 = [x**2 for x in [1,-1,2]] # 列表推导式
#
# print(sqt)
# print(sqt2)


"""练习"""
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
lis = ['ffewqgdsdsfsdfs','fds','fqfqfsq','ss','qq','tx','sssssWQ']
print([s.upper() for s in lis if len(s) >=3])

# 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
print([(x,y) for x in range(6) if x%2==0 for y in range(6) if y%2==1])

# 求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
M = [[1,2,3],[4,5,6],[7,8,9]]
print([r[2] for r in M])
