"""
    集合 set：可变数据类型  和 dict list一样
                但其中的元素必须是不可变数据类型
                无序，不重复  ---- 可用于列表去重
        应用：去除
"""

# 集合的创建
set1 = set({1,2,3})
set2 = {1,2,3}
# 如果内部元素为可变元素,会报错提示为内部有不可哈希的元素
# set3 = {1,'a', {'a':22,}}
print(set2)

""" 增加 """
# add(obj),无序的
set1.add('add')
print(set1)

# update(obj) 类似于list中的extend()，obj必须为可迭代对象，迭代后无序添加入set中
set1.update('activbate')
print(set1)

""" 删除 """
# pop() 随机删除set中的元素， 返回值为该元素
set1.pop()
print(set1.pop())
print(set1)

# remove(obj) 删除该元素，元素不存在则报错
set1.remove('add')
print(set1)

# clear() 清空集合, set()是空集合
# set1.clear()
# print(set1)

# del 删除

""" 没有改的方法 """

""" 查 """
for i in set1:
    print(i)

"""
集合的操作：
    1.交集    两种方法  & AND set1.intersection(set2)   返回值仍然是个集合
    2.并集    两种方法  | AND set1.union(set2)    返回值仍然是个集合
    3.反交集（除了交集中的元素以外的两个集合中的其他所有元素组成的集合）   
              两种方法  ^ AND set1.symmetric_difference(set2)
    4.差集(set1中独有的元素)    两种方法  set1-set2 AND set1.difference(set2)
    5.子集与超集      
        子集： set1 < set2     则称set1是set2的子集  两种方法： set1<set2 AND set1.issubset(set2)     返回bool值
        超集： set1 > set2     责成set1是set2的超集  两种方法： set1>set2 AND set1.issuperset(set2)   返回bool值
    6.frozenset(set) 将set转变为不可变类型<frozenset>,新的类型可遍历查询
"""
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# 交集
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # {4, 5}

# 并集
print(set1 | set2)
print(set1.union(set2))

# 反交集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))

set3 = {1,2,3}
set4 = {1,2,3,4,5,}

# 子集与超集
print(set3<set4)
print(set3.issubset(set4))

# frozenset(set)    使set转变为不可变类型 <frozenset>
set5 = frozenset(set3)
print(set5,type(set5))

# 去除 lis=[1,2,3,55,55,2,64,1,32,1,64,22,75,213]中重复元素，使用set和算法两种方法
# set()方法 元素顺序会改变
lis=[1,2,3,55,55,2,64,1,32,1,64,22,75,213]
# set1 = set(lis)
# lis = list(set1)
# print(lis)

# 算法 元素顺序不变
lis2 = []
for i in lis:
    if i not in lis2:
        lis2.append(i)
print(lis2)
