"""
    在控制台中循环录入学生信息（姓名，年龄，成绩 性别）
    如果名称输入空字符串，则停止录入
    将所有信息逐行打印出来
      # 使用 列表嵌套字典做
        [{“name”:姓名，"age":年龄，"result":成绩，"sex":性别}]
"""
"""
    在控制台中循环录入学生信息（姓名，年龄，成绩 性别）
    如果名称输入空字符串，则停止录入
    将所有信息逐行打印出来
    {   # 使用 字典嵌套字典做
        姓名：{"age":年龄，"result":成绩，"sex":性别}
    }
"""
# 学生信息 字典
list_student_info = []
dict_student_info = {}

while True:
    student_name = input("请输入学生姓名：")
    if student_name == "":
        break
    student_age = int(input("请输入学生年龄:"))
    student_reslut = float(input("请输入学生成绩:"))
    student_sex = input("请输入学生性别:")
    dict_student_info = {"name":student_name, "age":student_age, "result":student_reslut, "sex":student_sex}
    list_student_info.append(dict_student_info)


# 打印
# print(dict_student_info)
# print(list_student_info)

for item in list_student_info:
    print("{0}的年龄是{1}岁，成绩为{2}分，性别为{3}".format(item["name"], item["age"], item["result"], item["sex"]))


# 获取第一个学生的信息
list_student = list_student_info[0]
print("{0}的年龄是{1}岁，成绩为{2}分，性别为{3}".format(list_student["name"], list_student["age"], list_student["result"], list_student["sex"]))
