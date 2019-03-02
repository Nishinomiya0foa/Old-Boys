# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/2 0002 11:54'

"""
    文件处理
"""

# 打开文件  单一操作，文件不容易被破坏
# f = open('123.txt', 'r', encoding='utf-8')#  r w a   r+ w+ a+   b
    # 'r'，如果不填默认为'r'

# 操作文件
# 读
    # read()  ----全部读取
    # readlines()  ----全部读取，按行读取，放在列表
    # readline() ----读取一行；不方便用于读取视频图片
    # for循环  ----遍历 最好的

# 写
    # write()

# 光标  ----文件指针
    # seek(index)  ----指定光标的位置
    # tell()  ----获取当前光标位置
    # truncate(index)  ----截断

# 关闭文件
    # close()

# 修改文件
    # 没有修改文件的方法

    # 造成修改文件的假象
with open('test', 'r', encoding='utf-8') as f, open('test1.txt', 'w', encoding='utf-8') as f2:
    for line in f:
        if '陈文波' in line:
            line = line.replace('陈文波', '小白')
        f2.write(line)
    # 删除文件和重命名
import os
os.remove('test')  # 删除文件
os.rename('test1.txt', 'test.txt')  # 重命名文件