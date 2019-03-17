""" os模块  ---- 与操作系统交互的一个接口
和路径相关的操作都在os模块
"""

import os
# print(os.getcwd())  # 返回当前执行文件所在目录
# os.chdir('F:\Old Boys')  # 改变当前脚本的工作目录

# os.makedirs(path)  # 创建目录，可相对路径也可绝对路径
# os.removedirs(path)  # 递归删除路径，为空则删除，并返回到上级，空就再删
# os.mkdir(path)  # 创建单级目录
# os.rmdir(path)  # 删除单级子目录

# os.listdir(path)  # 打印path目录下，所有文件、子目录、隐藏文件
# os.remove(path)  # 删除一个文件
# os.renames(old, new)  # 重命名old文件，以new命名

# print(os.name)  # 输出当前操作系统类型 nt  posix

# os.system(command)  #执行系统命令。 直接打印
# ret = os.popen(command).read()  # 执行系统命令, 有返回值

# print(os.path.isfile(123))  # 判断一个路径是否文件
# os.path.isdir()  # 判断一个路径是否目录
# os.path.join(path1, path2, path3)  # 多级目录拼接

# os.path.getsize(path)  # 获取文件大小

