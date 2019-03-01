# 打开绝对路径文件
# f = open('C:\\Users\Administrator\Desktop\myfavourite.txt', 'r', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# 打开相对路径  ----在当前文件夹路径下

# 只读
# bytes -> str
# f2 = open('thisisafile', 'r', encoding='utf-8')
# print(f2.read())
# f2.close()

# 只写 w
# f3 = open('lgo.txt','w', encoding='utf-8')
# f3.write("i'm here! \tyou know \nanother line!")
# f3.close()

# 只写 wb
# f = open('lgo.txt', 'wb', )
# f.write('he呵呵he'.encode('utf-8')) # 将str的unicode类型，转换为utf-8类型
# f.close()

# 追加 a
f = open('lgo1.txt', 'a', encoding='utf-8')
f.write('bie啊')
f.close()

# 追加 ab
# f = open('lgo.txt', 'ab')
# f.write('qusi'.encode('utf-8'))
# print(f.read())
# f.close()


# with open('C:\\Users\Administrator\Desktop\myfavourite.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)