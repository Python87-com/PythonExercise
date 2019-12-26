list_stu_name = []
student_result = []
student_subject = ["数学", "语文", "英语"]
while True:
    result = []
    count = 0
    stu_name = input("请输入学生的姓名：")
    if stu_name == "q":
        break
    if stu_name in list_stu_name:
        print("学生姓名重复,请重新输入学习姓名!")
        continue
    while count < 3:
        stu_course = int(input("请输入学生{0}成绩：".format(student_subject[count])))
        if 0 > stu_course or stu_course > 100:
            print("请输入合法的学科成绩!!!")
            continue
        else:
            result.append(stu_course)
            count += 1
    list_stu_name.append(stu_name)
    student_result.append(result)
# result.clear()
for i in range(len(list_stu_name)):
    for item in student_result:
        average_score = sum(student_result[i]) / len(student_result[i])
    print("{0}的成绩如下：最高分{1}，最低分{2}，平均分{3}".format(list_stu_name[i], max(student_result[i]), min(student_result[i]),
                                                 average_score))

