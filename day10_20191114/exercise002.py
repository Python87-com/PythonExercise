"""
    练习：
"""


class Student:

    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_student(self):
        print("{}的年龄是{}岁，成绩为{}分，性别为{}".format(self.name, self.age, self.score, self.sex))


list01 = [
    Student("张三丰", 130, 96, "男"),
    Student("小龙女", 29, 92, "女"),
    Student("杨过", 26, 95, "男"),
    Student("丘处机", 35, 85, "男"),
    Student("李莫愁", 33, 86, "女")
]
list02 = [
    Student("张三丰", 130, 96, "男"),
    Student("小龙女", 29, 92, "女"),
    Student("杨过", 26, 95, "男"),
    Student("丘处机", 35, 85, "男"),
    Student("李莫愁", 33, 86, "女")
]


# 写一个函数，查找杨过的数据，将名字和年龄打印在控制台中
def lookup01():
    for item in list01:
        if item.name == "杨过":
            return item
    # return None


# stu = lookup01()
# print(stu.name, stu.age)


# 写一个函数，查找女性的数据，将名字和性别打印在控制台中
def lookup02():
    result = []
    for item in list01:
        if item.sex == "女":
            result.append(item)
    return result


stu = lookup02()

for item in stu:
    print(item.name, item.sex)


# 练习3 找出年龄大于30岁的有多少个
def lookup03():
    global count
    count = 0
    for item in list01:
        if item.age >= 30:
            count += 1
    return count


print(lookup03())  # 3


# 练习4 将list01中所有人的成绩归零
def lookup04():
    stu33 = []
    for item in list01:
        item.score = 0
        stu33.append(item)
    return stu33


stu3 = lookup04()

for item in stu3:
    print(item.name, item.score)


# 练习5  获取List01 中所有人的名字

def lookup05():
    list_name = []
    for item in list01:
        list_name.append(item.name)
    return list_name


stu4 = lookup05()

for item in stu4:
    print(item, end=" ")  # 张三丰 小龙女 杨过 丘处机 李莫愁
print(stu4)  # ['张三丰', '小龙女', '杨过', '丘处机', '李莫愁']


# 练习6 定义函数 在list01中查找年龄最大的人
def lookup06():
    stu_age = 0
    for item in list02:
        if stu_age < item.age:
            stu_age = item.age
    return stu_age


stu6 = lookup06()

print(stu6)
