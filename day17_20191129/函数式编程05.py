"""
    需求1：在列表中查找所有偶数
    需求2：在列表中查找所有大于10的数字
    需求3：在列表中查找所有范围在10-50之间的数
# 1. 使用生成器函数实现以上3个需求
# 2. 体会函数式编程的"封装"
#    将三个函数变化点提取到另外三个函数中.
#    将共性提取到另外一个函数中
# 3. 体会函数式编程的"继承"与"多态"
#    使用变量隔离变化点,在共性函数中调用变量.
# 4. 测试(执行上述功能)
"""

list01 = [13, 14, 20, 2019, 9, 128, 11, 28, 35, 48, 5, 6, 48, 12, 6]

# def find01():
#     for item in list01:
#         if item % 2 == 0:
#             print(item)
#
# find01()
print("--------------------------------")
# def find02():
#     for item in list01:
#         if item > 20:
#             print(item)
#
# find02()

print("--------------------------------")
# def find03():
#     for item in list01:
#         if 10 <= item <= 50:
#             print(item)
#
# find03()
print("---www--------------------------222---")


# ____________________________________________________
# 变化点

# "封装"
def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 20


def condition03(item):
    return 10 <= item <= 50


# “继承”
def find(func):
    for item in list01:
        # 多态
        # 调用：具体条件的抽象
        # 执行：具体条件的函数
        if func(item):
            yield item


# re = find(condition03)
# for item in re:
#     print(item)

for item in find(condition03):
    print(item)


# 方法参数,如果传递10/"张无忌"/True,叫做传递数据
# 方法参数,如果函数1/函数2/函数3,叫做传递逻辑