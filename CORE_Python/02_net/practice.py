"""面向连接的套接字和无连接的套接字的区别"""
# 即TCP和UDP的区别
# TCP：面向流，全双工,可靠，收到信息会有回复
# UDP：面向报文，不可靠，快

"""用自己的话描述 C/S 架构。 并给出几个例子"""
# server提供服务，接收client的请求，server会一直运行，一直处理client的请求
# 我们常见的有客户端的网游，客户端上显示丰富的界面，请求发送给server

"""TCP和UDP， 谁接收连接，并将它们转换到独立的套接字进行客户端通信"""

"""2-4 更新代码 使可以输入ip和port"""

"""2-5 C/S架构，tcp协议需满足更多功能。 识别以下命令： 
date:返回 time.ctime()
os:返回 os.name
ls:返回 os.curdir()
"""

import subprocess
import os

a = subprocess.call('dir', shell=True)
