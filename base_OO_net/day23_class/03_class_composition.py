"""组合
组合： 一个对象的属性值，是另外一个类的对象
"""
class Dog:
    def __init__(self, name, aggr, hp, kind):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.kind = kind

    def bite(self, person):
        person.hp -= self.aggr
        print('{dog}咬了{person},{person}掉了{losehp}血,还剩{lefthp}血'.format(dog=self.name, person=person.name,
                                                                       losehp=self.aggr,lefthp=person.hp))



class Person:
    def __init__(self, name, aggr, hp, gender):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.gender = gender
        self.money = 0
        self.weapon = None

    def attack(self, dog):
        dog.hp -= self.aggr
        print('{person}打了{dog},{dog}掉了{losehp}血,还剩{lefthp}血'.format(person=self.name, dog=dog.name,
                                                                     losehp=self.aggr, lefthp=dog.hp))

    def get_weapon(self, weapon):
        if self.money >= weapon.price:
            self.money -= weapon.price
            self.weapon = weapon  # 一个对象的属性是另外一个类的对象
                                #   alex  的 weapon 是  weapon类的对象knife
            self.aggr += weapon.aggr
        else:
            pass


class Weapon:
    def __init__(self, name, aggr, njd, price):
        self.name = name
        self.aggr = aggr
        self.njd = njd
        self.price = price

    def hand18(self, person):  # 定义一个技能
        if self.njd > 0:
            person.hp -= self.aggr*2
            self.njd -= 1


alex = Person('alex', 0.5, 100, '不详')
jin = Dog('jin', 50, 500, '不详')  # 由于实力不对等，考虑给alex增加一个装备
alex.money += 200
knife = Weapon('小刀', 100, 3, 150)  # 实例化了一把武器

print(alex.name,'充值了200')
alex.get_weapon(knife)  # alex装备了这把武器
# print(alex.weapon,alex.aggr)
jin.bite(alex)  # jin进攻
alex.attack(jin)  # alex进攻
alex.weapon.hand18(jin)  # 调用组合的方法
print(jin.hp)


# 栗子： 利用组合 写一个圆环类
class Circle:
    PI = 3.14

    def __init__(self,r):
        self.r = r

    def c_circle(self):
        """:return 周长"""
        return round(2*self.PI*self.r, 2)

    def s_circle(self):
        """:return 面积"""
        return self.PI*self.r**2


class Ring:
    def __init__(self,outside_r, inside_r):
        self.outside_c = Circle(outside_r)  # Circle类实例化后，赋值给outide_c,这里就是组合
        self.inside_c = Circle(inside_r)
        self.outside_s = Circle(outside_r)
        self.inside_s = Circle(inside_r)

    def s_ring(self):
        s = self.outside_s.s_circle() - self.inside_s.s_circle()
        return s

    def c_ring(self):
        c = self.outside_c.c_circle() + self.inside_c.c_circle()
        return c


a = Ring(20, 10)
print(a.s_ring())
print(a.c_ring())

# 创建一个老师类(name,gender,subject,)
# 老师有生日， 生日也可以是一个类 (date, weekday)
# 组合实现


# 面向对象的三大特性：继承 多态 封装

class Birth:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Course:  # 创建Couse的命名空间
    def __init__(self, teacher, subject, price):  # __init__放入命名空间
        self.teacher = teacher  # 在实例的命名空间
        self.object = subject
        self.price = price

    language = 'CHN'  # 静态属性  # language放入命名空间；language在类命名空间中

    def func(self):  # 方法  func放入命名空间
        pass


class Teacher:
    def __init__(self, name, gender, subject,birth):
        self.name = name
        self.gender = gender
        self.subject = subject
        self.birthday = birth
        self.course = Course('huang', 'code', 18990)  # 可以直接这儿实例化


xiaoming_b = Birth(2019,3,21)
# course = Course('huang', 'code', 18990)  # 也可以这儿传参
xiaoming = Teacher('黄晓明', 'MALE', 'Python', xiaoming_b)
print(xiaoming.birthday.month)
print(xiaoming.course.price)
print(xiaoming.course.language)

