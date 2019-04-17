"""
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

伪代码：

for p in 目录a：
    if p==目录：
        遍历p
    else:
        print


"""

import os





def print_filename(path):
    first_path = os.listdir()
    for i in first_path:
        # print(i)
        if os.path.isdir(os.path.join(path,i)):
            print_filename(i)
            return i
        elif os.path.isfile(i):
            print(i)


if __name__ == '__main__':
    path = r'F:\learning\遍历文件'
    print_filename(path)