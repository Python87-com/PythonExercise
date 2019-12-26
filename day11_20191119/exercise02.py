"""
    小明在招商银行取钱
"""


class Person:
    def __init__(self, name, money):
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

    # 去银行存钱
    # def go_money(self, str_position, type):
    #     print(self.__name, "取钱")
    #     type.go_run(str_position)


class Bank:
    def __init__(self, name, money):
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

    # 取钱
    def draw_money(self, person, value):
        """
            取钱
        :param person: 人
        :param value: 取钱数
        """
        self.money -= value
        person.money += value
        print(person.name, "在", self.name, "取了%d钱" % value)


# 调用
# 创建一个人   名字   存款
s1 = Person("小明", 0)
# 创建一个银行  名称     银行有多少钱
bank = Bank("招商银行", 5000000)

bank.draw_money(s1, 5000)
