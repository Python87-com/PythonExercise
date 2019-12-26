"""
 属性私有化
"""


class Student:
    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def play(self):
        print(self.name, "性别是", self.__sex)


# 创建对象
s1 = Student("Python87", "女")
s1.play()   # Python87 性别是 女
s1.__sex = "男"
s1.play()   # Python87 性别是 女



