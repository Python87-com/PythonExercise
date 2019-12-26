"""
3. 请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    思考：变化点是数据的不同还是行为的不同。
"""


class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Work:
    def __init__(self, money):
        self.money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def working(self, person, value):
        self.money -= value
        person.money += value
        print(person.name, "工作赚了", value)


# 创建 & 调用
s1 = Person("赵敏")
s2 = Person("张无忌")
sb = Work(60000)

# 赵敏　上班　挣了　6000
sb.working(s1, 6000)

# 张无忌　上班　挣了　10000
sb.working(s2, 10000)