"""
    列表的增删改查
        1.列表本身被改动了
    公共方法：

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
list1[0:2] = '陈文波11'
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
print(list1.index('文'))

# 排序 reverse=True 倒序；否则正序
list2 = [3,1,5,3,67,2,1]
list2.sort(reverse=True)
print(list2)

list2 = [3,1,5,3,67,2,1]
# 反转
list2.reverse()
print(list2)
