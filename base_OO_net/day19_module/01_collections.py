"""collections  ---- 扩展数据类型,里面有许多常用的其他数据类型
堆栈：先进后出
队列：先进先出  FIFO

"""

# namedtuple  ---- 可命名元组

# from collections import namedtuple
# point = namedtuple('pont', ['x', 'y'])  # 声明一个可命名元组类型叫point，其中有一个元素叫pont，内部包含两个元素(x,y)
#                                         # 一次定义，多次调用
# p = point(2,3)  # 创建 point()类型的数据
# p2 = point(-3,5)
# print(p.x)  # 访问方式
# print(p2.y)
# print(p)


"""queue  ---- 队列:先进先出"""
# import queue
# q = queue.Queue()  # 创建队列q，不可迭代
# print(q.qsize())  # 输出q的大小
# q.put(5)  # 输入元素
# q.put(4)  # 输入元素
# q.put(3)
# print(q.get())  # 第一个取出的元素是最先输入的;如果队列中已经没有元素了，再执行get()方法，会阻塞。直到有新的元素传入



""" deque  ---- 双端队列,左侧和右侧能同时进行类似队列的操作
                 ---- 能高效插入和删除
 """
#
# from collections import deque
# dq = deque([1,2])
# dq.append(3)  # 从后面放入数据  [1,2,3]
# dq.appendleft(-1)  # 从前面放入数据 [-1,1,2,3]
# dq.insert(2,'a')  # 按照索引插入  [-1,1,'a',2,3]
# print(dq.pop())  # 从后面取出数据
# print(dq.pop())  # 从后面取出数据
# print(dq.pop())  # 从后面取出数据
# print(dq.popleft())  # 从前面取出数据


""" ordereddict 有序字典
                ---- 用法和普通字典一样，只是有序了
"""
# from collections import OrderedDict
# od = OrderedDict([('a', 1), ('b', 2)])  # OrderedDict([(key, value), (key, value), (key, value)])

""" defaultdict 默认字典"""
# from collections import defaultdict
# d = defaultdict(lambda : 5)  # 创建默认字典时，需指定所有默认的value的类型,该类型必须是可调用的
#                         # 或者可以利用 匿名函数 lambda，则返回不可调用的数据类型
# print(d['k1'])

""" Counter 计数器"""
from collections import Counter
l = ['a','a','b','bb','ccc']
c = Counter(l)  # 返回l内各元素出现的次数 Counter类型
print(c)