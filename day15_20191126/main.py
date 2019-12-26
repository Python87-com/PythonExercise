"""
案例：
my_ project /
main.py
common/
    __init__.py
	double_list_helper.py
	list_helper.py
skill_system/
    __init__.py
    skill_deployer.py
    skill_manager.py
练习:
1.在main.py中调用skill_deployer.py。
2.在skill_deployer.py中调用skill_manager.py。
3.在skill_manager.py中调用double_list_helper.py。
4.在list_helper.py中调用main.py。
要求：在所有的调用过程中，要包含函数、类、实例方法、静态方法。
14：45
"""
from skill_system.skill_deployer import *


class MainTest(object):
    @staticmethod
    def print_main():
        print("print-----MainTest")


# 1.在main.py中调用skill_deployer.py。

s1 = Student("张三", 25)
s1.fly()  # 张三 25
