"""
    练习
    for i in range(10):
        print(i)
"""


class MyRange:
    pass


class MyRangeManager:
                        # 开始数字   终止数字    步长
    def __init__(self, startNum=0, stopNum=0, stepNum=1):
        self.startNum = 0
        self.stopNum = 0
        self.stepNum = 1
        self.__list_ruange = []

    def add_myrange_num(self, num):
        self.__list_ruange.append(num)

    def __iter__(self):
        return MyRangeIterator(self.__list_ruange)


# 迭代器


class MyRangeIterator:
    def __init__(self, target):
        self.__target = target

    def __next__(self):
        pass


# ------------------------------------------


m01 = MyRangeManager()
m01.add_myrange_num(1, 10, 1)
m01.add_myrange_num(11)
m01.add_myrange_num(13)

# 获取迭代器
iterator = m01.__iter__()
# 获取迭代器内下一个数据
item = iterator.__next__()
print(item)

for i  in range(10):
    print(i)
