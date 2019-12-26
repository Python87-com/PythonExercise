"""
    定义一个 圆 类

    圆面积计算公式：S = pi * r ** 2
"""


class Circular(object):
    # 类属性
    PI = 3.14

    def __init__(self, r):
        self.r = r

    # 计算圆的面积
    def calculated_area(self):
        if isinstance(self.r, (int, float)):
            print("圆的面积为:{0}".format(Circular.PI * self.r ** 2))
        else:
            print("请输入合法的数值")


# 定义一个圆
c1 = Circular(20.001)
c1.calculated_area()
