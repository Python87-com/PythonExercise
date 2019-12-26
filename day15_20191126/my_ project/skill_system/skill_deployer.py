from skill_system.skill_manager import *


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        print(self.name, self.age)


# 2.在skill_deployer.py中调用skill_manager.py。
re = print_d(5)

print(re)  # 3125