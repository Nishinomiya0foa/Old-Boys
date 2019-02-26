"""
    列表的增删改查
        增加：
            1.append(obj) 增添一个元素到列表末尾
            2.insert(index, obj) 增添一个元素到index索引前
            3.extend(iterable) 添加一个可迭代对象，迭代后至于列表末尾
        删除：
            1.pop(index) 删除该索引的元素，默认最后一个
            2.remove(obj)  删除列表中该元素，不存在则报错
            3.clear() 清空列表
            4.del list 删除列表
            5.del list[i:j] 可以切片删除
        改：
            1.list[i]=obj 替换
            2.list[i:j]=iterable 切片修改替换为可迭代对象，被迭代后添加。
        查：
            1.for ... in list 遍历
            2.可切片查询
    公共方法：
        1.len() count(obj) index(obj) 同str。 返回长度，元素出现数量，元素索引
        2.sort(reverse=False) 默认reverse=False，升序/ True则降序;按首字母的ASCII码顺序排序
        3.reverse() 列表翻转
    元组：只读列表，可循环查询，可切片
        1.元组内元素不能直接被修改。 如果内部元素为list，则该list可被修改
    range:
        1.range(10,1,-1) 步长，倒序

"""
import time
list1 = ['web', 'yueer', 'feifei', 'xiaoquan']

# 增加 append()
list1.append('kuikui')
list1.append(1)

print(list1)

# 增加n个目标
# while 1:
#     new_empleyee = input(">")
#     if new_empleyee != 'q':
#         list1.append(new_empleyee)
#         print("{}正在被录入。。。".format(new_empleyee))
#         time.sleep(2)
#     else:
#         print("录入完毕")
#         break
# print(list1)

list1 = ['web', 'yueer', 'feifei', 'xiaoquan']
# 增加 insert()  插入到索引之前
list1.insert(1, "xiaokui")
print(list1)

# extend()  插入一个可迭代对象， 被迭代之后加入到末尾
list1.extend([1,2,3])
print(list1)

"""
    删除元素
"""
list1 = ['web', 'yueer', 'feifei', 'xiaoquan']
# pop() 删除索引的值,返回这个值；默认删除最后一个
# list1.pop(-1)
# print(list1.pop(1))
# print(list1)

# remove() 按value值删除

list1.remove('web')
print(list1)

# clear()  清空列表
list1.clear()
print(list1)

list1 = ['web', 'yueer', 'feifei', 'xiaoquan']
# del 删除
del list1

list1 = ['web', 'yueer', 'feifei', 'xiaoquan']
# 可以切片删除
del list1[0:2]
print(list1)

"""
    改
"""
list1 = ['web', 'yueer', 'feifei', 'xiaoquan']
list1[0] = 'wenbo'
print(list1)

# 切片修改 修改的被迭代添加
list1 = ['web', 'yueer', 'feifei', 'xiaoquan']
list1[0:2] = '123'
print(list1)

"""
    查
"""
# 遍历
# for ... in list

# 切片查询


"""公共方法"""
# len()
print(len(list1))

# count()
print(list1.count('1'))

# index() 返回索引
# print(list1.index('文'))

# 排序 reverse=True 倒序；否则正序
list2 = [3,1,5,3,67,2,1]
list2.sort(reverse=True)
print(list2)

list2 = [3,1,5,3,67,2,1]
# 反转
list2.reverse()
print(list2)


"""
    列表嵌套
    
"""
list1 = ['web', 'yueer', '非非', 'xiaoquan',['xiaoer','sanwei','bing']]
list1[0] = list1[0].capitalize()
print(list1)

# 将'sanwei'大写


list1[4][1] = list1[4][1].upper()
print(list1)


"""
    元组
"""
tup1 = ('web', 'yueer', '非非', 'xiaoquan',['xiaoer','sanwei','bing'])
for i in tup1:
    print(i, end= ' ')

# 改动元组中嵌套的列表中的元素
tup1[4][1] = 3
print()
print(tup1)

print(','.join(['web', 'yueer', 'feifei', 'xiaoquan']))

#
for i in range(10,-1,-1): # 不会报错 输出为空
    print(i)


# 打印 list1 = ['web', 'yueer', '非非', 'xiaoquan',['xiaoer','sanwei','bing']]
# 中所有元素

list1 = ['web', 'yueer', '非非', 'xiaoquan',['xiaoer','sanwei','bing']]
for i in list1:
    if type(i) != type(list1):
        print(i)
    else:
        for j in i:
            print(j)


# *
# **
# ***
# ****
# *****

for i in range(5):
    print('*'*(i+1))

list1[4].append('ilo')
print(list1)

del list1

list1 = []
list1.append(1)
print(list1)