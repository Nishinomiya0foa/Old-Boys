"""内置方法"""

# property  内置装饰器函数，只在面向对象中使用
# 可以把方法伪装成属性，调用方式就变成了属性的调用方式
# class Circle:
#     """定义圆
#     :returns 周长和面积
#     """
#     PI = 3.14
#     def __init__(self, r):
#         self.r = r
#
#     @property       # 使用property装饰器, 将get_s的调用方式变成属性的调用方式;这样就不能进行传参了
#     def get_s(self):
#         return self.PI * self.r**2
#
#     @property
#     def get_c(self):
#         return 2 * self.PI * self.r

# c1 = Circle(5)
# print(c1.get_s)  # 如果没有property装饰器，get_c()是一个方法。
                # 但有了property装饰器后，get_c就直接是他的方法的返回值了


# 例子 BMI指数
"""
例一：BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
"""
class BMI:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property  # 使bmi方法的调用方式变为属性的调用方式。
    def bmi(self):
        bmi_num = self.weight / (self.height ** 2)
        if bmi_num < 18.5:
            return '过轻'
        elif 24 > bmi_num >= 18.5:
            return '{}的BMI指数：正常 {}'.format(self.name, round(bmi_num, 2))  # 保留小数
        elif 24 <= bmi_num < 28:
            return '过胖'
        elif 28 <= bmi_num < 32:
            return '肥胖'
        elif 32 <= bmi_num:
            return '过于肥胖'

# chen = BMI('陈文波', 71, 1.79)
# print(chen.bmi)

# 通过@property使方法转变成了属性。
# 如果想在外部改变被修改成属性的这个方法的值
# class Circle:
#     """定义圆
#     :returns 周长和面积
#     """
#     PI = 3.14
#     def __init__(self, r):
#         self.r = r
#
#     @property       # 使用property装饰器, 将get_s的调用方式变成属性的调用方式;这样就不能进行传参了
#     def get_s(self):
#         return Circle.PI * self.r**2
#
#     # 我想修改PI的值，改为外部定义的新pi的值
#     @ get_s.setter    # 用于新设定一个值， 仅限1个，不能少不能多
#                       #  只能用在@property后， 且名字一定是@property处的方法名.setter
#     def get_s(self, pi):  # 定义一个@property处的同名方法，接受一个参数
#         Circle.PI = pi  # 用接收的参数进行赋值
#
# c1 = Circle(5)
# c1.get_s = 3  # 指定 @get_s.setter处的参数
# print(c1.get_s)

# property实际应用
# 定义一个商品类 属性：名字 价格
# 突然商品降价 全场5折
# class Goods:
#     __discount = 0.6
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.__discount
#
#
# apple = Goods('苹果', 5000)
# print(apple.price)


# 属性可以 查看 修改 删除
# 删除 有点像 方法名.setter
            # 删除：  @方法名.deleter  ---- 这个只是在外部使用del方法时，触发了这个装饰器函数。执行内部逻辑
                                    # 他本身不能做任何删除的操作。只是可以进入执行代码而已！
            # @方法名.deleter
            # def 方法名(self):
            #     def self.私有属性
# 这样就可以外部删除类中私有属性
