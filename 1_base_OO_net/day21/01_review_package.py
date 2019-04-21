""" 包：package
导入包时，自动执行__init__.py文件
"""
# python2.7中， 只有带有__init__.py才能成为一个包

# import 从包中导入模块
# import glance.api.policy as policy  # 点的左边必须是包
# glance.api.policy.get()
# policy.get()

# from A.B.C import D
# 不能是 from A.B import C.D  ---- import后不能带点（.）
# from glance.api import policy
#
# policy.get()

# 绝对路径： 不能改变文件夹逻辑，但是直观
# import glance时，希望能执行glance包中的所有方法。
# 需要在其中所有的__init__.py中，import同级的所有模块
import glance
glance.api.versions.create_resource('haha')


# 相对路径：  .  ---- 指当前路径
#            ..  ---- 指上级路径
# 只能在包外使用
# 可以随意移动包，只要包的整体路径保持，就能进行调用
# 如果使用了相对路径，包里的模块想调用包里的其他模块时，只能通过相对路径了
# 但不能在包体内直接调用包里的所有模块，可以在外部进行使用