"""
    在控制台中循环录入学生信息（姓名，年龄，成绩 性别）
    如果名称输入空字符串，则停止录入
    将所有信息逐行打印出来
    {   # 使用 字典嵌套字典做
        姓名：{"age":年龄，"result":成绩，"sex":性别}
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
    dict_student_info[student_name] = {"age":student_age, "result":student_reslut, "sex":student_sex}

# 打印
for name, values in dict_student_info.items():
    print("{}的年龄是{}岁，成绩为{}分，性别为{}".format(name, values["age"], values["result"], values["sex"]))
