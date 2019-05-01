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
import time



def count_lines(path, count=0):
    dir_list = os.listdir(path)

    for file in dir_list:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            count_lines(file_path)
        elif os.path.splitext(file_path)[1] == '.py':
            with open(file_path,'r', encoding='utf-8') as f1:
                for line in f1:
                    # print(line.strip())
                    if not line.lstrip().startswith('#') and line.strip() != '':
                        # print(line.strip())
                        count += 1
            print(file_path, ':', count)
        count = 0


def getlines(path):
    file_list = os.listdir(path)

    for file in file_list:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            getlines(file_path)
        else:
            print(file_path)


if __name__ == '__main__':
    path = r'F:\Old Boys'
    # print(count_lines(path))
    getlines(path)