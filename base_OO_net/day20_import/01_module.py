"""模块
        ---- import模块后，直接执行
import 模块名  # 创建一个独立的命名空间，保存着xxx里的全部命名
    调用  ---- 模块名.变量名
import 模块名 as 简称  # 对模块重命名；可以对拥有同样方法的多个模块命名同一个别名，这样后续操作简便，提高代码兼容性
    调用  ---- 简称.变量名
from 模块名 import 变量名_a/*  # 把模块的变量名_a或者全部导入，不能和本文件重名，会冲突
    调用  ---- 变量名
__all__ = ['xxx']  # 被导入的模块中如果有__all__，from 模块名 import *中就只会导入被__all__收录的命名

__name__  ---- 模块中有__name__变量，当直接执行这个模块时，__name__==__main__；
                                    当在其他模块中引用这个模块时，__name__==这个模块名

import规则：
先import 内置模块
再import 扩展模块
最后import 自定义模块

"""



# 执行import时，先从sys.modules里找，如果已经被导入，就不再导入了；如果没有，就一句sys.path路径寻找模块

from demo import read as rd

# rd()

