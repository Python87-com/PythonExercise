"""
    在控制台中循环录入学生信息（姓名，年龄，成绩 性别）
    如果名称输入空字符串，则停止录入
    将所有信息逐行打印出来
    {   # 使用 字典嵌套列表做
        姓名：[年龄，成绩，性别]
    }
"""
# 学生信息 字典
dict_student_info = {}

while True:
    student_name = input("请输入学生姓名：")
    if student_name == "":
        break
    student_age = int(input("请输入学生年龄:"))
    student_reslut = float(input("请输入学生成绩:"))
    student_sex = input("请输入学生性别:")
    dict_student_info[student_name] = [student_age, student_reslut, student_sex]

# 打印
for name, values in dict_student_info.items():
    # 注意，这里 [年龄，成绩，性别] 是存在列表中的，想要取出来，可以使用索引的方式
    print("{}的年龄是{}岁，成绩为{}分，性别为{}".format(name, values[0], values[1], values[2]))