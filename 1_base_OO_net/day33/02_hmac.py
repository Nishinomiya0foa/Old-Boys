"""客户端合法性验证"""
# 不依赖登录验证
# 利用hmac模块
#   server和client有一个公用的密钥，server发送一个msg，同时加密一下这个msg
#   client接收到这个msg，用hmac模块加密之后发回server
#   server接收client发回的加密过的secret_msg，与自己的加密过得msg比对，相同则client合法。

import hmac

h = hmac.new(b'potato', b'egg')  # hmac.new(b'密钥'，b'密文')
secret = h.digest()
print(secret)

import socket
