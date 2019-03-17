# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2019/3/16 0016 15:09'

import os

path = 'F:\python old boys\ALL_oldboys_film_from_BILIBILI\\'
result = os.listdir(path)
print(result)

for file in result:
    if 's9' in file:
        os.renames(path+file, path+file.replace('s9', ''))