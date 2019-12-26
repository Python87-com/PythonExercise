"""
    练习：定义函数，数值相加的函数
"""


def adds(*args):
    result = 0
    for item in args:
        result += item
    return result
    # return sum(args)

print(adds(1, 3, 5, 7, 9))  # 25
