"""

"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]


class Vector2:
    """
        二维向量
        可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 静态方法：表示左边方向
    @staticmethod
    def left():
        return Vector2(0, -1)

    # 静态方法：表示右边方向
    @staticmethod
    def right():
        return Vector2(0, 1)


# 作用 位置 + 方向

pos01 = Vector2(1, 2)

# 通过类名调用静态方法
l01 = Vector2.left()

pos01.x += l01.x
pos01.y += l01.y

print(pos01.x, pos01.y)
