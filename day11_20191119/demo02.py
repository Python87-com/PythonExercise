"""

"""


class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # 本质：障眼法（实际变量名称被改为：_类名__age）
        # self.__age = age
        self.set_age(age)
        # self.__weight = weight
        self.set_weight(weight)

    # 提供公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 10 <= value < 100:
            self.__age = value
        else:
            raise ValueError("年龄输入有误")

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 30 <= value < 60:
            self.__weight = value
        else:
            raise ValueError("体重输入有误")



