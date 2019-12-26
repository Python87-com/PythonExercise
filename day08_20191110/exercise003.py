"""
    练习  定义 根据成绩判断等级 的函数
result = float(input("请输入您的成绩："))

# 逻辑
if 90 <= result <= 100 :
    print("您的成绩为：优秀")
elif 79 < result < 90:
    print("您的成绩为：良好")
elif 69 < result < 80:
    print("您的成绩为：中等")
elif 59 < result < 70:
    print("您的成绩为：及格")
elif 0 <= result < 60:
    print("您的成绩为：不及格")
else:
    print("您输入的成绩有误，请重新输入。")

"""

def achievementGrade(number):
    grade = ["优秀","良好","中等","及格","不及格","成绩有误"]
    if 90 <= number <= 100:
        return grade[0]
    elif 79 < number < 90:
        return grade[1]
    elif 69 < number < 80:
        return grade[2]
    elif 59 < number < 70:
        return grade[3]
    elif 0 <= number < 60:
        return grade[4]
    else:
        return grade[5]

# 调用函数
reslut = achievementGrade(95)

print(reslut)