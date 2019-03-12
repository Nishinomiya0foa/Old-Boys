"""几个重要内置函数"""

# all(a)  ---- 判断a中所有元素的bool值是否全为True，a必可迭代
# print(all([1,0,2,3,4,5]))

# any(a)  ---- 判断a中所有元素的bool值是否有值为True，a必可迭代
# print(any([1,0,2,3,4,5]))

# zip(*args)  ---- 返回一个迭代器;args都可迭代;返回的迭代器中每一个元素都由原args中对应索引位置的元素组成的元组；长度为min(*args)
# a = (1,2,3)
# b = ['a','b','c']
# c = 'zx'
# for i in zip(a,b,c):
#     print(i)

"""filter() 过滤"""
"""
filter() 过滤
1.结构
    filter(func, iterable)  ---- func函数的返回值为True，迭代iterable每个元素执行func，True则保留；False则舍去
                            ---- func可以使内置函数，也可以是用户声明的函数
2.返回值                           
    ---- filter()返回的是列表
     ---- 过滤之后的元素个数，小于等于原来iterable对象中的元素个数 
3.例子
# 请利用filter()过滤出1~100中平方根是整数的数
def get_sqrt(num):
    return (num**0.5)%2==1

print(filter(get_sqrt, range(1, 101)))


map()   
1.结构
    map(func, iterable)  ---- func接受iterable中每一个元素，进行func处理后，返回一个可迭代类型。
2.作用
    ---- 对iterable中每一个元素，进行func函数处理，不改变原iterable对象元素的个数。
3.例子
# 求元组中每个元素的平方根
def get_sqrt(x):
    return x**0.5
    
print(list(map(get_sqrt, (1,9,16,27))))

                           



"""
#  ----filter筛选后的元素个数 <= 筛选前原来的元素个数
# filter(func,iterable)  ---- 迭代iterable，每个值去执行func。如果func的返回值为True，保留该元素；False则舍去该元素
#                        ---- 返回列表

# 筛选出元组中的所有奇数
# def get_odd(nums):
#     return nums%2 == 1
# odd_nums = list(filter(get_odd, (3,1,2,21,52,123,5,3)))
# print(odd_nums)



# 筛选出列表中所有字符串元素
lis = ['123',123,'zxc','我',True]
# def get_str(x):
#     # return x == '{}'.format(x)
#     return type(x) == type('str')
# str_lis = list(filter(get_str, lis))
# print(str_lis)

# 请利用filter()过滤出1~100中平方根是整数的数。效果应等同于以下执行的结果：print([x for x in range(1,101) if (x**0.5)%1==0])
# def get_sqt(x:str):
#     """"""
#     return (x**0.5)%1 == 0
# str_lis = list(filter(get_sqt, range(1,101)))
# print(str_lis)

"""map()"""
#  ---- map前后元素个数不变，但每个元素的值可能有变化
# a = ['a','b','c']
# def double_a(x):
#     return x*2
# rev_a = map(double_a, a)
# print(tuple(rev_a))

# sorted(obj, key, reverse)  # 排序算法。 会直接生成原来的序列，返回列表或元组等；快，占内存
                            # 对obj进行排序，关键字为key，reverese=True则从大到小
# l = [1,23,421,452,2]
# a = sorted(l,reverse=True)
# print(a)

# 列表按照每一个元素的len排序
# l = ['adadfsds','fdsf2er1221','xxx!']
# sorted_l = sorted(l,key=len)
# print(sorted_l)



