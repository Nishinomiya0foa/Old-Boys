# reversed(obj)  ---- 返回obj被翻转后的迭代器
# print(list(reversed([1,2,3,4])))

# slice(start,end,step)  ---- 返回切片的索引，从start到end，步长step
# l = [1,2,324,534,1,213,54,5]
# l2 = slice(1,6,2)
# print(l[l2])
# # 效果等同 l[1:6:2]

# format()  ---- 格式化输出,有多重用法:http://www.cnblogs.com/Eva-J/articles/7266245.html  详细介绍

# bytes(obj)  ----将obj转换为bytes类型
# print(bytes('哈哈哈',encoding='utf-8'))  # unicode转换为utf-8的bytes
    # 应用：编码；网络通信；文件存储；html中爬取的内容也是bytes类型

# bytearray()  ---- byte类型的数组

# memoryview()  ----

# ord(obj)  ----返回obj(单个字符)的编码值
# chr(obj)  ----返回ASCII码对应的字符
# print(ord('$'))
# print(chr(99))

# repr(obj)  ----保留obj的数据类型
# print('{},你好'.format('chen'))

# set() frozenset()  ---- 集合；不可变集合