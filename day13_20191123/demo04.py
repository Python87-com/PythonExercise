"""
    继承和多态
    开闭原则

    老张开车去东北，用面向对象的方式
"""


# 定义一个交通工具父类，约束子类行为
class Vehicle():
    # 定义一个 运输方法
    def transport(self, str_position):
        pass


# 客户端代码，用交通工具。
class Person:
    def __init__(self, name):
        self.name = name

    # 去的方法
    def go_to(self, vehicle, str_position):
        # 多态：调用父，执行子.
        # 调用的是交通工具的运输方法
        # 执行的是飞机的运输方法或者汽车的运输方法
        vehicle.transport(str_position)


# -----------以上为架构师写的代码---------------------以下为程序员写的代码-----------------------------------
class Car(Vehicle):
    def transport(self, str_position):
        print("开汽车去", str_position)


class Electrocar(Vehicle):
    def transport(self, str_position):
        print("骑电动车去", str_position)


class Train(Vehicle):
    def transport(self, str_position):
        print("坐火车去", str_position)


# ---------------------------------------------------------------
# 调用
p01 = Person("老张")
# v01 = Vehicle()
c01 = Car()
t01 = Train()
e01 = Electrocar()
# v01.transport("东北")
p01.go_to(c01, "北京")
p01.go_to(t01, "上海")
p01.go_to(e01, "南京")
