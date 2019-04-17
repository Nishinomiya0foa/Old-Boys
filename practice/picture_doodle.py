"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

# 16位， 大小写英文+数字， 每4位用 - 分离
# ascii   97-122  65-90
# 0-9

import random

def getcode(n):
    with open('200codes.txt', 'w', encoding='utf-8') as f1:
        for num in range(n):
            lis = []
            for x in range(97, 123):
                lis.append(chr(x).upper())
                lis.append(chr(x))
                if x < 107:
                    lis.append(x-97)

            code = ''
            for i in range(1,17):
                code = code+ str(random.choice(lis))
                if i % 4 == 0 and i != 16:
                    code = code + '-'

            f1.write('{}\n'.format(code))

if __name__ == '__main__':
    getcode(200)

