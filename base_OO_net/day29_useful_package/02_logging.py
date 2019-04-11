"""
logging 日志
非常重要
用来记录用户行为 或者 代码的执行过程
可以是： debug时 或 用户行为 或 程序出错

日志能够开关，可控

"""

# import logging
#
# # 5个级别 按严重性: critical > error > warning > info > debug/notset
# logging.debug('debug message')  # 出错，处理细节，值的内容
# logging.info('info message')  # 普通信息，正常打印的内容，一般为用户操作
# # 默认打印以下重要性的log
# logging.warning('warning message')  # 警告
# logging.error('error message')  # 错误，影响程序运行的
# logging.critical('critical message')  # 致命

# 配置日志打印格式
# basicconfig：简单，能做的事相对少
    # basicconfig 会出现中文乱码
    # 不能同时输出到文件和屏幕
# 配置log对象：稍微复杂，但能做更多的事  ---- 尽量采用这种
    # 低耦合 程序高度定制

# basicconfig
import logging

# basicconfig 会出现中文乱码
# 不能同时输出到文件和屏幕
# logging.basicConfig(level=logging.INFO,  # 打印DEBUG级别以上的log
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 输出内容格式化
#                     datefmt='%a, %d %b %Y %H:%M:%S',  # 格式化时间输出
#                     filename='test.log',  # 控制写入到文件
#                     filemode='a')  # 文件打开方式
#
# try:
#     int(input('num>'))
# except ValueError:
#     logging.error('ValueError!')

# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

import logging

logger = logging.getLogger()

formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')  # 定制日志显示格式
# formatter2 = logging.Formatter('{} / {} / {} / {}'.format(asctime, name, levelname, message))

# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息

fh = logging.FileHandler('test.log', encoding='utf-8')  # 文件读写类型 默认为 a
sh = logging.StreamHandler()  # 输出到屏幕类型

# 文件句柄和格式关联
fh.setFormatter(formatter)  # 文件句柄和格式关联
sh.setFormatter(formatter)  # 绑定格式

# 设置日志级别
logger.setLevel(logging.DEBUG)  # 总共的级别
fh.setLevel(logging.INFO)  # 分别设置 文件打印的级别
sh.setLevel(logging.NOTSET)   # 屏幕输出的级别


#
logger.addHandler(fh)  # logger对象 和 文件句柄fh关联
logger.addHandler(sh)  # logger对象 和 屏幕输出sh关联

logger.debug('debug message')  # 出错
logger.info('info message')  # 普通信息
logger.warning('warning message')  # 警告
logger.error('error message')  # 错误
logger.critical('critical message')  # 致命
