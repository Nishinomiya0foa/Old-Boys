"""hashlib模块
    非常常用
"""
# 摘要算法  有md5  sha1等
# MD5 能被撞库破解
# 一般用作登录验证，
# 文件的一致性验证  ---- 检查下载的文件与远程服务器的文件是否一致
            #       ---- 检查两台机器上的两个文件是否相等
import hashlib
# md5 = hashlib.md5()
# md5.update(b'12345')
# print(md5.hexdigest())

# 算法不同。摘要的功能特性不变
# 对相同字符串使用同一摘要算法得到的值始终是相同的。
# 算法的使用方法一样

# pwd = input('>')
# md5 = hashlib.md5()
# md5.update(bytes(pwd, encoding='utf-8'))  # 加密的数据必须为bytes类型
# pwd_sec = md5.hexdigest()
#
# with open('test', 'r', encoding='utf-8') as f1:
#     for line in f1:
#         if pwd_sec==line.strip():
#             print(True)

"""MD5 能被撞库破解，这是他不够安全的地方"""

# 可以对加密算法进行加盐，安全性会更高
md5 = hashlib.md5(bytes('陈文波',encoding='utf-8'))
md5.update(b'123456')
print(md5.hexdigest())

"""动态加盐:可以使用用户名的一部分作为盐；前提是用户名不可修改。"""

# hashlib用法
import hashlib
md5 = hashlib.md5()  # 创建一个md5对象
md5.update(b'123')
md5.update(b'456') # 分成两块进行摘要算法的结果和 一起的事一样的
print(md5.hexdigest())

# 作业： 对一个文件进行摘要算法，最后计算出这个文件的md5值