"""
# 练习：员工管理器记录多个员工
#      迭代员工管理器对象
"""


# 员工类
class Employee:
    pass


# 员工管理器
class EmployeeManager:
    """
        员工管理器 可迭代对象 （参与for）
    """
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    # 添加员工
    def add_employee(self, value):
        self.__employees.append(value)

    def __iter__(self):
        return EmployeeIterator(self.__employees)


# 迭代管理器
class EmployeeIterator:
    """
        员工迭代器  获取下一个数据
    """
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp

# 创建员工
manager = EmployeeManager(Employee())
manager.add_employee("张三")
manager.add_employee("李四")
manager.add_employee("王五")
manager.add_employee("赵倩")


# ——————以下为  多 态
# 获取员工迭代器
employeeIter = manager.__iter__()

# 获取员工数据
while True:
    try:
        item = employeeIter.__next__()
        print(item)
    # 遇到异常则退出循环
    except StopIteration:
        break
