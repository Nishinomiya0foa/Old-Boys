# 类名开头一般是大写
class Dog:
    def __init__(self,name,health,aggr,type):
        self.name = name
        self.health = health
        self.aggr = aggr
        self.type = type

    def bite(self, person):
        """狗的咬人方法，人被咬"""
        person.health -= self.aggr
        if person.health <= 0:
            print('{}被{}咬了一口， 死了'.format(person.name, self.name))
        else:
            print('{}:我咬了{}一口,他掉了{}血, 还剩{}血'.format(self.name, person.name,
                                                self.aggr, person.health))

class Person:
    def __init__(self, name, health, aggr, gender):
        self.name = name
        self.health = health
        self.aggr = aggr
        self.gender = gender

    def attact(self,dog):
        """人打狗"""
        dog.health -= self.aggr
        if dog.health <= 0:
            print('{}被{}打了一下， 死了'.format(dog.name, self.name))
        else:
            print('{}:我打了{}一下，它掉了{}血，还剩{}血'.format(self.name, dog.name,
                                               self.aggr, dog.health))


wenbo = Person('chen', 100, 100, 'MALE')
hobby = Dog('hobby', 100, 20, 'teddy')  # 两个类各实例化一个对象

hobby.bite(wenbo)  # hobby咬wenbo
wenbo.attact(hobby)  # wenbo打hobby


# circle类  属性：r   方法：求周长  方法：求面积
class Circle:
    PI = 3.14
    def __init__(self,r):
        self.r = r

    def c_circle(self):
        """:return 周长"""
        return round(2*self.PI*self.r, 2)

    def s_circle(self):
        """:return 周长"""
        return self.PI*self.r**2

c1 = Circle(5)
print(c1.r)
print(c1.c_circle())
print(c1.s_circle())


class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def s_rect(self):
        return self.a * self.b

    def c_rect(self):
        return 2*(self.a+self.b)

r1 = Rectangle(3,5)
print(r1.s_rect())
print(r1.c_rect())