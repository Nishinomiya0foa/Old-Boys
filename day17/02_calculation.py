"""算法
    ---- 查找 排序 最短路径等问题的解决方法等
"""



# 二分查找算法  必须处理有序的列表

# 使用二分查找法 查找到66的索引值
l = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,111,122]
# 这样找到的索引值肯定为0，这是因为在递归调用的过程中，随着函数被切片，索引顺序已经被破坏了
# def find_num(l,aim):
#     mid_index =len(l)//2
#     if l[mid_index] < aim:
#         new_l = l[mid_index+1:]
#         find_num(new_l,aim)
#     elif l[mid_index] > aim:
#         new_l = l[:mid_index]
#         find_num(new_l, aim)
#     else:
#         print('found it',mid_index,l[mid_index])
#
#
# find_num(l, 66)

#
def find_num(l, aim, start=0, end=None):
    end = len(l) if end is None else end
    mid_index = (end-start)//2 + start
    if start <= end:
        if l[mid_index] < aim:
            return find_num(l, aim, start=mid_index+1, end=end)
        elif l[mid_index] > aim:
            return find_num(l, aim, start=start, end=mid_index-1)
        else: return mid_index
    else:
        return '111'
# print(find_num(l, 223))

# 自己过一下 两次就能找到的  多次才能找到的  不存在在数组中的
# 三级菜单的代码
# 考试附加题
# 默写递归算法

# 阶乘 递归实现
def jiecheng(n):
    if n > 1:
        return n * jiecheng(n-1)
    else:
        return 1
print(jiecheng(6))