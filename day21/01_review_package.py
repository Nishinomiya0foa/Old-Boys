""" 包：package """
# python2.7中， 只有带有__init__.py才能成为一个包

# 从包中导入模块
import glance.api.policy as policy  # 点的左边必须是包
# glance.api.policy.get()
policy.get()

# from ... import
from glance.api import policy

policy.get()