"""
    练习：随意创建一个 手机类
    注意：变量名称 不能和 函数名称 一样；
    如果一样，使用 类名.函数名(对象)  是可以调用的，但是使用 对象名.函数名 是会报错的
    品牌 价格 颜色
"""


class Phone():

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def phone_color(self):
        print("{0}手机的颜色多数都是{1}的。".format(self.brand, self.color))

    def phone_price(self):
        print("{0}手机价格是{1}".format(self.brand, self.price))


# 创建手机
apple = Phone("Apple", "black", 7000)

# 调用
apple.phone_color()       # Apple手机的颜色多数都是black的。
Phone.phone_price(apple)  # Apple手机价格是7000
Phone.phone_color(apple)  # Apple手机的颜色多数都是black的。

"""
apple1.color()  报错？？   变量名  不能 和  函数名一样？
TypeError: 'int' object is not callable
TypeError:“int”对象不可调用
"""
