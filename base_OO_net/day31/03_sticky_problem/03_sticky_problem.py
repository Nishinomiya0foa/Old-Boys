"""黏包问题  只有TCP会出现黏包
        ---- 发送方发送的若干数据到接收方接收时,黏成一包,从接收缓冲区看,后一包的头紧挨前一包的尾
TCP协议的拆包机制：如果本机的MTU超过网关的MTU，大的数据包就会被拆开来传送。产生许多数据包碎片，增加丢包率
出现原因:
    1.发送方原因：TCP的Nagle算法
                        1.只有上一个分组得到确认，才会发送下一个分组
                        2.收集多个小分组，在一个确认到达时一起发送
    2.接收方原因：接收方没有一次性取出所有的包，结果下一次从缓冲区取数据时，取出的是上次的遗留数据，造成黏包
"""



# 远程执行命令
# 所有的客户端执行server端下发的命令

# import subprocess
# #                       命令    shell执行    输出结果保存到PIPE     错误信息保存到PIPE
# res = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# # 取stdout中的信息，控制台默认gbk
# r_stdout = res.stdout.read().decode('gbk')
# # 取stderr中的信息
# e_stderr = res.stderr.read().decode('gbk')
#
# print('stdout:',r_stdout)
# print('stderr:',e_stderr)