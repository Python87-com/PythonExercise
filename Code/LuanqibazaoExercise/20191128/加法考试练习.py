"""
    10以内加法考试
    需求：1、界面选项菜单： 1 加法考试 2 减法考试 3 比大小考试 4 查看错题
        2、初始成绩为0，每次考试提取20道题目，答对+5分，答错不加分
"""
import random

# 成绩类变量()
user_count = 0

# 图形界面 UI  view 视图
class UserUi:
    print("小朋友，欢迎来到学前模拟考试界面,请在家长的陪同下考试哦！！！")
    print("1 加法考试 2 减法考试 3 比大小考试 4 查看错题")
    userInput = print("请输入你的选项")
    while True:
        if userInput == '1':
            AddOperation.operation()




# 运算
class Operation:
    def operation(self):
        pass


# 数字生成器
class NumIterator:

    def num_create(self):
        x1 = random.randint(1, 6)
        y1 = random.randint(1, 6)
        return [x1, y1]


# ----------Control 控制------------------
# 加法运算

class AddOperation(Operation):
    def __init__(self):
        self.__list_num = []

    def operation(self):
        return self.__list_num[0] + self.__list_num[1]



# 减法运算
class SubOperation(Operation):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operation(self):
        return self.x - self.y


# 比大小运算
class BigOrSmallOperation(Operation):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operation(self):
        return self.x + self.y


add01 = AddOperation()
add01.operation()