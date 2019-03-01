"""
1.文件操作
    打开文件的过程： 'myfavourite.txt'
    1.文件路径，可以是绝对路径或相对路径
        ‘C:\Users\Administrator\Desktop\myfavourite.txt’
    2.编码方式：
        以何种编码方式保存的文件，就要以同样的编码方式打开
        utf-8,gbk
    3.操作方式： 只读，只写，追加，读写，写读...
        只读：
            r: 1.不能进行修改，只能查看
            rb  ----bytes类型打开（应用：1.打开非文字类的文件；2.上传下载文件）
        只写：
            w: 1.文件不存在则新建文件。2.文件存在则清空原文件，再写入
            wb：1.不用加编码类型。2.写入的str需将unicode类型，转换为utf-8类型
                # 只写 wb
                f = open('lgo.txt', 'wb', )
                f.write('he呵呵he'.encode('utf-8')) # 将str的unicode类型，转换为utf-8类型
                f.close()
        追加：添加到源文件末尾,不可读
            a：1.文件不存在则新建文件
            ab:

"""
