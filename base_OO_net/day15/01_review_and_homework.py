"""复习迭代器、生成器 和 作业讲解"""

"""迭代器"""
# 可迭代协议
# 迭代器协议
# 特点  ----节省内存空间
#       ----方便逐个取值，一个迭代器只能取值一次

"""生成器"""  # ----本质也是迭代器
# 生成器函数
    # 含有yield关键字的函数，都是生成器函数
    # 特点：调用之后，函数内的代码不执行，返回一个生成器；没有进行取值时，执行一段代码（--yield），遇见yield停止。
    # 取值方式：
        # __next__();每次next取值一个
        # for 循环：取出全部值，除非有判定条件
        # send():不能用于第一个yield，取下一个值时，给上一个yield传递一个值
            # 需要预激活，可用装饰器
        # 数据类型强制转换：将全部的值都读到这个数据类型对应的内存里
# 生成器表达式
    # 想放入生成器中的值/i for i in iterable if 条件


"""作业"""
# 处理文件。用户指定要查找的文件和内容。将文件中包含要查找的内容的每一行。输出
# def search_content(filename, content):
#     try:
#         with open(filename, 'r', encoding='utf-8') as f1:  # 句柄：handler
#             for line in f1:
#                 if content in line:
#                     print(line.strip())
#     except:
#         print('文件可能不存在！')
# search_content('homework', 'work')

# 写生成器，从文件中读取内容。每一条包含work的内容前加上 '***'，返回
# def readfile_g(filename):
#     with open(filename, 'r', encoding='utf-8') as f1:
#         for line in f1:
#             if 'work' in line:
#                 yield '***'+line.strip()
#             else:
#                 yield line.strip()
#
# g = readfile_g('homework')
#
# for word in g:
#     print(word)