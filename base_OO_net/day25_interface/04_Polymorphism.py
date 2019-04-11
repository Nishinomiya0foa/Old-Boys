"""多态 Polymorphism
多态：多个不同的类具有共同的方法func，调用方法func，得到的返回值不同。
        把这个方法func提取出来，封装为一个接口g。不同类的实例作为参数传入接口g，得到不同的返回值
python，天生支持多态,是多态语言，python崇尚鸭子类型。
鸭子类型：不崇尚继承父类或实现接口而拥有方法或属性，而是依据其本身的方法或属性的集合决定
            例如： list类和tuple类，非常相似，也没有采用继承的方式
    优点：低耦合
    缺点：太过自由
python是一门动态强类型语言。
"""

class WeChat:
    def pay(self, money):
        print('使用wechat支付了{}元'.format(money))


class Alipay:
    def pay(self, money):
        print('使用Alipay支付了{}元'.format(money))

def pay(pay_obj, money):  # 统一支付入口
    pay_obj.pay(money)