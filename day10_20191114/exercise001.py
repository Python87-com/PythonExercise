"""
1、创建学生类
    ----数据：
    ----行为：
2、在控制台中循环录入学生信息，如果名字是空字符，退出
3、在控制台中输出每个学生的信息（调用打印学生类的打印方法）
4、打印第一个学生信息
"""


class Student:

    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_student(self):
        print("{}的年龄是{}岁，成绩为{}分，性别为{}".format(self.name, self.age, self.score, self.sex))


# ssk = Student("ssk", 28, 99, "女")
# ssk.print_student()


list_student_info = []
while True:
    student_name = input("请输入学生姓名：")
    if student_name == "":
        break
    student_age = int(input("请输入学生年龄:"))
    student_score = float(input("请输入学生成绩:"))
    student_sex = input("请输入学生性别:")
    stu = Student(student_name, student_age, student_score, student_sex)
    list_student_info.append(stu)


# 打印
for stu in list_student_info:
    # Student.print_student(stu)
    stu.print_student()