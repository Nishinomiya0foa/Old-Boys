"""类和对象 命名空间"""


class Course:  # 创建Couse的命名空间
    def __init__(self, teacher, subject, price):  # __init__放入命名空间
        self.teacher = teacher  # 在实例的命名空间
        self.object = subject
        self.price = price

    language = 'CHN'  # 静态属性  # language放入命名空间；language在类命名空间中

    def func(self):  # 方法  func放入命名空间
        pass

python = Course('cwb', 'python', 19800)
math = Course('zl', 'math', 5555)
python.language = 'ENG'  # 对自身的命名中新赋值一个language，其实并不是修改类中静态属性。  ---- 只针对不可变数据类型
                        # 对于不可变数据类型，类变量最好用类名操作
                        # 对于可变数据类型，修改是共享的。重新赋值是独立的
print(python.language)  # 类中的静态变量，可以被对象和类调用
print(math.language)
print(python.language)


# 举例说明，可变数据类型可以被实例修改
# 栗子：爸妈分别赚钱，钱需要增加
# class Family:
#     money = 0
#
# mother = Family()
# father = Family()
# mother.money+=1000
# print(mother.money)
# father.money+=1000
# print('money:', Family.money)  # 由于类中静态变量不能被实例修改，所以尽管爸妈分别赚钱了，Family中的钱却仍为0

# 静态变量使用可变数据类型呢？
class Family:
    money = [0]  # 可变数据类型 list

mother = Family()
father = Family()
mother.money[0] +=1000  # 对原有列表进行修改
father.money[0] +=1000
print('money:', Family.money[0])  # 被修改成功


# 练习  每实例化一个对象， 计数+1
# 最终所有对象共享这个数据
class CountNum:  # 类的命名 --- 驼峰式命名。 单词首字母大写
    count = 0

    def __init__(self):
        CountNum.count += 1


a = CountNum()
b = CountNum()
print(a.count)
print(b.count)
c = CountNum()
print(c.count)


# 认识绑定方法
# 对象调用方法时， 该方法就是该对象的绑定方法

