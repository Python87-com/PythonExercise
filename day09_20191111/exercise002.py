"""
    练习：创建一个随意的学生类
"""


class Student():

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("{0}，今天学校吃了红烧肉".format(self.name))

    def learn(self):
        print("{0}，我已经在学习了哈".format(self.name))


# 创建学生
ssk = Student("SSK", 29, "男")
qtx = Student("qtx", 39, "男")
mpp = Student("mpp", 28, "女")

# 调用方法
ssk.eat()           # SSK，今天学校吃了红烧肉
mpp.learn()         # mpp，我已经在学习了哈

Student.eat(qtx)    # qtx，今天学校吃了红烧肉