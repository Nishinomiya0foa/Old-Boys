"""
1.文件操作

    打开文件的过程： 'myfavourite.txt'
    1.文件路径，可以是绝对路径或相对路径
        ‘C:/Users/Administrator/Desktop/myfavourite.txt’
    2.编码方式：
        以何种编码方式保存的文件，就要以同样的编码方式打开
        utf-8,gbk
    3.操作方式： 只读，只写，追加，读写，写读...
        读： 若文件不存在，则报错;打开文件后，光标位于（0，0）位置
            r:  只读  ---- 1.不能进行修改，只能查看
            rb: 只读  ---- bytes类型打开（应用：1.打开非文字类的文件；2.上传下载文件）
            r+: 读写  ---- 1.先读后写的情况：先读出原文件内容，存入内存，然后从读结束的地方开始写；这是因为读完之后，光标移动至
                             读的末尾的位置
                           2.先写后读的情况：先从（0，0）位置开始覆盖着写，写完之后，从写的末尾读出之后的内容；也是因为写完之后，光标
                             移动到了写的末尾的位置、
                             PS：先写后读时，如果文件使用的是utf-8编码，即一个中文字符占用三个字节，如果再使用英文进行覆盖填写，
                                 如果覆盖中文字符的英文不是正好>=3个字符，会造成乱码情况
            r+b:读写（bytes类型）
        写：  若文件不存在则新建文件;打开文件后，光标位于（0，0）位置
            w:  1.则清空原文件，再写入
            wb：1.不用加编码类型。2.写入的str需将unicode类型，转换为utf-8类型
                # 只写 wb
                f = open('lgo.txt', 'wb', )
                f.write('he呵呵he'.encode('utf-8')) # 将str的unicode类型，转换为utf-8类型
                f.close()
            w+: 1.先写后读，写之前清空文件；
            w+b: （bytes）
        追加： 添加到源文件末尾,不可读;打开文件后，光标位于文件最末尾位置
            a：1.文件不存在则新建文件
            ab: bytes
            a+: 1.文件不存在则新建文件
                2.若要读文件内容需调整光标位置
2.调整光标位置
    f.seek(index)
"""

