"""封装
私有属性和方法不被子类继承
"""
# 例子
class Room:
    def __init__(self, owner, length, width):
        self.owner = owner
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width  # 内部调用私有属性

# chen = Room('陈文波', 12, 8)
# print(chen.get_area())

# 用到私有概念的场景
#     1.不想从外部调用
#     2.不想让属性被改变
#     3.保护属性不被子类继承
