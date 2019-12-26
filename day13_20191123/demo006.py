"""
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置

"""


# 图形管理器
class GraphicsManager:
    def __init__(self):
        self.__graphic = []

    # 添加图形
    def add_graphic(self, graphic):
        if not isinstance(graphic, Graph):
            raise ValueError("不是图形")
        self.__graphic.append(graphic)

    def get_total_area(self):
        total_area = 0
        # 遍历图形列表，累加每个图形的面积
        for item in self.__graphic:
            total_area += item.calculate_area()
        return total_area

    # def draw(self, graph_target):
    #     if not isinstance(graph_target, Graph):
    #         raise ValueError
    #     print("开始计算")
    #     graph_target.calculate_area()


# 定义一个 Graph 父类
class Graph:
    # 计算面积方法
    def calculate_area(self):
        # 如果子类中没有area方法，则抛出异常
        raise NotImplementedError


# _________________________________________________________

# 定义一个圆形类
class Roundness(Graph):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # S = 3.14 * radius ** 2
        # print("圆的面积为：", S)
        return 3.14 * self.radius ** 2


# 定义一个矩形类
class Rectangle(Graph):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        # S = self.length * self.width
        # print("矩形的面积为：", S)
        return self.length * self.width


# _______________________________________________
# 图形管理器
gg01 = GraphicsManager()

r01 = Rectangle(15, 42)
r02 = Roundness(31)
# 加进图形管理器
gg01.add_graphic(r01)
gg01.add_graphic(r02)

# 计算总面积
re = gg01.get_total_area()

print(re)