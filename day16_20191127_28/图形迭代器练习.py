"""
   练习：图形管理器记录多个图形
   迭代图形管理器对象
"""


class Graphic:
    pass


# 图形迭代器
class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果index超出范围则停止
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        # 获取元素
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


# 图形管理器
class GraphicManager:
    def __init__(self):
        # 存放图形的列表
        self.__graphics = []

    def add_graphic(self, value):
        self.__graphics.append(value)

    def __iter__(self):
        return GraphicIterator(self.__graphics)


# 创建图形
t01 = GraphicManager()
# 添加图形
t01.add_graphic("正方形")
t01.add_graphic("矩形")
t01.add_graphic("圆形")

# 获取迭代器
iterator = t01.__iter__()

# 获取每一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
