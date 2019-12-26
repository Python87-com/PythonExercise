"""
    创建一个类
"""


class Wife():
    # 数据成员
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 行为成员
    def play(self):
        print(self.name, "在玩耍。")


# 创建对象
ssk = Wife("ssk", 30)

# 调用对象
ssk.play()
