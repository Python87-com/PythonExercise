"""
    定义员工管理器
        1.管理所有员工
        2. 计算所有员工工资 calculator_salary

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.
"""


# 员工管理器
class EmployeeManager:
    # 定义一个存储所有员工的列表
    def __init__(self):
        self.__all_employees = []

    # 添加员工
    def add_employee(self, all_employees):
        # 判断是不是员工，是员工才存储
        if not isinstance(all_employees, Employee):
            raise ValueError("不是员工的子类")
        self.__all_employees.append(all_employees)

    # 计算所有员工工资
    def calculator_salary(self):
        """
            计算所有员工工资
        :return:累加后的工资总和
        """
        total_employee_salary = 0
        # 遍历所有员工列表，累加员工工资
        for item in self.__all_employees:
            total_employee_salary += item.salary()
        return total_employee_salary


# 员工 父类
class Employee:
    def __init__(self, basic_salary):
        """
            获取软件测试工资组成信息
        :param basic_salary: 基本工资
        """
        self.basic_salary = basic_salary
    # 工资方法
    def salary(self):
        # 如果子类没有重写或者没有计算工资方法，则抛出异常
        raise NotImplementedError


# ______________________________________________________
# 所有员工类  子类 继承 父类    子类重写父类计算工资方法

# 子类的参数只能从自己的 __init__中获取，不能问父类要
# 程序员
class Programmer(Employee):
    # 序员：底薪 + 项目分红
    def __init__(self, basic_salary, deduction_wage):
        """
            获取程序员工资组成信息
        :param basic_salary: 基本工资
        :param deduction_wage: 项目分红
        """
        super().__init__(basic_salary)
        self.deduction_wage = deduction_wage

    def salary(self):
        """
            计算程序员工资
        :return: 基本工资 + 项目分红
        """
        return self.basic_salary + self.deduction_wage


# 销售
class Sales(Employee):
    # 销售：底薪 + 销售额saleroom * 0.05
    def __init__(self, basic_salary, saleroom):
        """
            获取销售工资组成信息
        :param basic_salary: 基本工资
        :param saleroom: 销售总额度
        """
        super().__init__(basic_salary)
        self.saleroom = saleroom

    def salary(self):
        """
            计算销售工资
        :return: 基本工资 + 提成
        """
        # 这里的 0.05 也可以做成一个参数/变量，防止日后 变化 0.07 0.12之类的提成率上升，或者针对不同销售，提成不一样
        return self.basic_salary + self.saleroom * 0.05


# 增加一个新的岗位 软件测试   基本工资 + 绩效奖（工资的10%）
# 软件测试
class Testing(Employee):
    def __init__(self, basic_salary):
        """
            获取软件测试工资组成信息
        :param basic_salary: 基本工资
        """
        super().__init__(basic_salary)

    def salary(self):
        """
            计算工资
        :return: 基本工资 + 绩效
        """
        return self.basic_salary + self.basic_salary * 0.1


# ______________________________________________________
# 测试
e01 = EmployeeManager()

# 销售 6000 + 500000 * 0.05 = 25000 = 31000
s01 = Sales(6000, 500000)

# 程序员   12000 + 5600 = 17600
p01 = Programmer(12000, 5600)

# 软件测试 9000 + 900 = 9900
t01 = Testing(9000)
# 添加员工
e01.add_employee(s01)
e01.add_employee(p01)

re = e01.calculator_salary()
print(re)  # 48600.0
# ______________添加软件测试后_________________
e01.add_employee(t01)
re = e01.calculator_salary()
print(re)  # 58500.0