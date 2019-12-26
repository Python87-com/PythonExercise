"""
    练习：定义对象计数器
    定义老婆类，创建3个老婆对象
    可以通过类变量记录老婆对象个数
    可以通过类方法打印老婆对象个数
"""


class Wife:

    # 定义类变量
    wife_count = 0

    @classmethod
    def w_count(cls):
        print(cls.wife_count)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Wife.wife_count += 1


# 创建老婆
wife01 = Wife("赵敏", 29)
wife02 = Wife("苏明玉", 27)
wife03 = Wife("小龙女", 22)

# 可以通过类变量记录老婆对象个数
print(Wife.wife_count)  # 3

# 可以通过类方法打印老婆对象个数
Wife.w_count()      # 3