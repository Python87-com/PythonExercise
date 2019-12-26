list01_name = []
list02_total = []
while True:
    subject = ["数学", "语文", "英语"]
    name = input("请输入学生姓名：")
    list01_name.append(name)
    list03_temp = []
    for i in range(3):
        while True:
            score = int(input("请输入%s的%s成绩：" % (name, subject[i])))
            if score < 0 or score > 100:
                print("输入错误")
            else:
                list03_temp.append(score)
                break
    list02_total.append(list03_temp)
    end = input("需要结束程序吗？按q")
    if end == "q":
        break
print("--------------------------------------------------")
for j in range(len(list01_name)):
    print("%s的总分是%d" % (list01_name[j], sum(list02_total[j])))
    print("最高分是%d" % (max(list02_total[j])))
    print("最低分是%d" % (min(list02_total[j])))
    print("平均分是%d" % (sum(list02_total[j]) / len(list02_total[j])))
