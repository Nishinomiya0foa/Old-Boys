"""复习"""
# 1.组合：
class Course:
    def __init__(self,name,price,period):
        self.price = price
        self.period = period
        self.name = name
python = Course('Python', 19800, '6 month')

class Classes:
    def __init__(self,name,course, teacher,school):
        self.name = name
        self.course = course
        self.teacher = teacher
        self.school = school

chuer = Classes('初二',python, '小王', '北大')  # 组合
print(chuer.course.price)

# 面向对象的三大特征：继承 多态 封装

# 命名空间：类和对象分别存在不同的命名空间。
    # 对象中可以调用类命名空间中的名字；类不能调用对象的

# 继承：
#   单继承  ：super只能在py3中使用。 super是根据mro广度优先找上一个类
#         父类：
#         子类：调用时先用自身命名空间中的，如果没有，再用父类命名空间的
    # 多继承
    # 抽象类和接口类

    # 经典类：深度优先
    # 新式类：广度优先 。   这就是python3中的类 继承Object

# 多态和鸭子类型

# 封装

# 三个装饰器
#     @property   @类名.setter
#     @classmethod
#     @staticmethod  # 当一个方法只使用了类的静态变量时，就给他加上@classmethod装饰器。默认传cls参数