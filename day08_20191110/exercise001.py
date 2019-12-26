"""
    定义一个 四位数 每个位相加和 的函数
"""

# 定义函数
def add(num01):
    #         千位                百位                  十位              个位
    return num01 // 1000 + num01 // 100 % 10 + num01 // 10 % 10 + num01 % 10

int_num01 = int(input("请输入一个四位数的整数："))

# 调用函数
total = add(int_num01)
print("您输入的数是{0}，每位数相加的和为：{1}".format(int_num01, total))
