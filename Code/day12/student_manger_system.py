"""
    学生信息管理系统
        实现对学生信息的增加、删除、修改和查询。
"""


# 数据模型类：
class StudentModel:
    def __init__(self, name, age, score, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


# 逻辑控制类：
class StudentManagerController:
    # 定义一个类变量id，用于初始化学生id
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    # 添加学生
    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 一个没有编号的学生信息
        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        """
            学生ID编号生成
        :return: 返回一个不重复的id
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    # 根据id删除学生
    def remove_student(self, id):
        """
            根据id编号删除学生信息
        :param id: 学生编号
        :return: bool [True 删除成功 False 删除失败]
        """
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
            return True
        return False

    # 根据id修改学生信息
    def update_student(self, stu_info):
        """
            根据 stu_info.id 来修改学生信息
        :param stu_info: 学生对象
        :return: bool  True 成功  False 失败
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    # 排列顺序

    def order_by_score(self):
        """
        根据成绩，对self.__stu_list进行升序排列
        :return:
        """
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


# 界面视图类：
class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        """
        逻辑控制对象
        """
        self.__manager = StudentManagerController()

    # 显示菜单
    def __display_menu(self):
        print("欢迎使用学生信息管理系统")
        print("1)添加学生|2)显示学生|3)删除学生|4)修改学生|5)按照成绩升序显示学生|")

    # 选择菜单
    def __select_menu(self):
        item = input("请输入操作编号：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()
        else:
            print("请正确输入操作编号！！！")
            print("-" * 50)

    # 程序界面入口
    def main(self):
        """
        界面视图入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    # 输入学生信息
    def __input_students(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        score = float(input("请输入学生成绩："))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    # 输出学生信息
    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    # 删除学生
    def __delete_student(self):
        id = int(input("请输入需要删除的学生编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    # 修改学生信息
    def __modify_student(self):
        # stu = StudentModel()
        # stu.id = int(input("请输入需要修改学生的编号："))
        # stu.name = input("请输入需要修改学生的姓名：")
        # stu.age = int(input("请输入需要修改学生的年龄："))
        # stu.score = float(input("请输入需要修改学生的成绩："))
        id = int(input("请输入需要修改学生的编号："))
        name = input("请输入需要修改学生的姓名：")
        age = int(input("请输入需要修改学生的年龄："))
        score = float(input("请输入需要修改学生的成绩："))
        stu = StudentModel(name, age, score, id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    # 按成绩输出学生
    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


view = StudentManagerView()
view.main()
"""

# 测试开始
s1 = StudentModel("zs", 26, 99, 0)
manager = StudentManagerController()
manager.add_student(s1)
manager.add_student(StudentModel("1zs", 26, 69, 0))
manager.add_student(StudentModel("2zs", 26, 85, 0))
manager.add_student(StudentModel("3zs", 23, 79, 0))
for item in manager.stu_list:
    print(item.id, item.name)
print("---------------------------------")
# 删除学生
# print(manager.remove_student(1001))
# for item in manager.stu_list:
#     print(item.id, item.name)

# 修改学生信息
manager.update_student(StudentModel("张三", 26, 69, 1001))
for item in manager.stu_list:
    print(item.id, item.name, item.age, item.score)
# 测试结束
"""
