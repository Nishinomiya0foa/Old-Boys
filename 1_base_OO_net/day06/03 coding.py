"""

"""

"""
ASCII:
    'A' = 一个字符 = 1个字节（bytes） = 8位（bit）

Unicode:
    'A' = 一个字符 = 4个字节（bytes） = 32位(bit)
    '国' = 一个字符 = 4个字节（bytes） = 32位(bit)

utf-8:
    'A' = 一个字符 = 1个字节（bytes） = 8位
    '国' = 一个字符 = 3个字节（bytes） = 8位
    
gbk：
    'A' = 一个字符 = 1个字节（bytes） = 8位
    '国' = 一个字符 = 2个字节（bytes） = 8位

"""

"""
编码encode()：  编码是指将 unicode ->  utf-8/gbk
    1.各种编码之间的二进制是不能互相识别的，会乱码
    2.文件的储存和传输不能为unicode，可以是utf-8/utf-16/gbk/gb2312等。这是因为unicode占用的空间过大
py3:
    1.str在内存中的编码方式是unicode
        bytes类型：使用utf-8等编码。 
        str类型的存储和传输依赖转换为bytes类型
        
        英文中：
            str：表现形式 s = 'abc'
                 内部存储 01010001 unicode
            bytes：表现形式 s = b'abc'
                    内部存储 01010001 utf-8 gbk... 
        中文中：
            str：表现形式 s = '中国'
                 内部存储 01010001 unicode
            bytes：表现形式 s = b'x\e91\e91\e91\e91\e91\e91'   ----如果1个中文字符占用3个\e91类型则为utf-8编码；占用2个，则为gbk编码
                    内部存储 01010001 utf-8 gbk...    
    将 str -> bytes：
        s1_str = 'abc'
        s1_bytes = s1_str.encode('utf-8')     # encode(obj)是编码, obj为编码类型
        
        s2_str = '中国'
        s2_bytes = s2_str.encode('utf-8')   # utf-8中一个中文字符占用3个字节，gbk中一个中文字符占用2个字节
"""
s2_str = '中国'
s2_bytes = s2_str.encode('gbk')
print(s2_bytes)