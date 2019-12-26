"""
    自定义异常
        练习:敌人类(攻击力0--100)
        抛出异常的信息：消息/错误行/攻击力/错误编号
"""


class Enemy:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def print_info(self):
        print(self.name, self.age)


e01 = Enemy("孙悟空", 888)
e01.print_info()
