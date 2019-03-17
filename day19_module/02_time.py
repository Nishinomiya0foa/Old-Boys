""" time  ---- 时间模块 """


import time

# time.sleep(n)  # 暂停n秒
# time.time()  # 返回时间戳浮点数，表示当前时间；需要格式化输出. 从19700101 00:00:00开始 至今经历的秒数

"""表示时间格式的3中方式
时间戳：从19700101开始 至今经历的秒数  ---- 计算机方便统计
格式化输出的字符串：形如 1970-01-01 21:00:01  ---- 人类方便看
结构化时间struct_time: struct_time中共九个元素 
                      (年，月，日，时，分，秒，一年中第几周，一年中第几天，等等)  ---- 方便人类统计
"""

"""时间戳"""
# print(time.time())


"""格式化时间字符串  ---- 方便观看"""
# print(time.strftime('%Y-%m-%d %H:%M:%S'))  # time.strftime() 格式化输出时间的方式
#                                      # '%Y-%m-%d %H:%M:%S' 是一种格式化  输入形如：2019-03-16 16:36:26
# print(time.strftime('%c'))

# 所有的格式化符号
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

""" 结构化时间 ---- 元组"""
# struct_time = time.localtime()
#                             # 输出形如：
#                             # time.struct_time(tm_year=2019, tm_mon=3, tm_mday=16, tm_hour=16, tm_min=46,
#                             #                   tm_sec=1, tm_wday=5, tm_yday=75, tm_isdst=0)
# print(struct_time.tm_wday)  # 可以用 struct_time.tm_year  访问内部变量


""" 三种时间显示的相互转换 """
"""时间戳与结构化时间"""
# t = time.time()  # t是时间戳
# # localtime() 用于将 时间戳 -> 结构化时间

# print(time.localtime(t))  # 本地的结构化时间
# print(time.gmtime(t))  # 格林尼治的结构化时间

# mktime()  结构化时间 -> 时间戳
# l = time.localtime()  # l是结构化时间
# print(time.mktime(l))  #

# strptime(time, format)  # 格式化时间 -》 结构化时间
p = time.strptime('2019.3.16', '%Y.%m.%d')  # p是结构化时间

f = time.strftime('%Y{}%m{}%d'.replace('{}', '-'), p)  # f是格式化时间
print(f)

