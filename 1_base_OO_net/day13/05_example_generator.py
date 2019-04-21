"""
生成器应用：
例子：监听文件输入
"""

def tell(file):
    with open(file, 'r', encoding='utf-8') as f1:
        while True:
            line = f1.readline().strip()
            if line:
                yield line

g = tell('file')
for i in g:
    if 'shi' in i:
        print('file 文件中包含shi的行有：',i)
    if '十' in i:
        print('file 文件中包含时的行有：',i)