"""
小数据池：
    int  ->  (-5, 256)
    str  ->   1.无特殊字符

ASCII:
    一个字符（只有英文） = 1字节（bytes） = 8位（bit）
unicode：
    一个字符（任意字符） = 4bytes = 32 bit
utf-8：
    一个字符（中文） = 3bytes = 24 bit
gbk：
    一个字符（中文） = 2bytes = 16bit

除了unicode英文表示为4bytes，其余编码英文都为1bytes

"""

"""
1.基础数据类型汇总补充：
    str
    int
    bool
    tuple：不可变数据类型   元组中如果只有1个元素，需要在其后加，表示
    list：可变数据类型
    dict：可变数据类型, dict迭代时，其长度不能变化
        可变数据类型在被迭代时，不要改变其长度
2.集合set
3.深浅copy
"""
# str = '1 '
# print(str.isspace())

lis1 = [0,1,2,3,4,5]
for i in range(len(lis1)): # 会报错；因为list是可变数据类型，循环中改变了lis1的长度。索引的大小就超过了列表的长度
    del lis1[i]

lis1 = [0,1,2,3,4,5]
# for i in lis1:
#     if lis1[lis1.index(i)] % 2 == 0:
#         del lis1[lis1.index(i)]
# print(lis1)
print(len(lis1) % 2)


for i in range(len(lis1)-2, -1, -2):
    del lis1[i]

print(lis1)

dic = {
    'k1': 'v1',
    'k2': 'v2',
    'name': 'Sad',
}
# 删除字典key中包含'k'的键值
temp_lis = []
for i in dic.keys():
    if 'k' in i:
        temp_lis.append(i)
for i in temp_lis:
    dic.pop(i)
print(dic)