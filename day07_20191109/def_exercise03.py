"""
    在控制台中打印一维列表的函数
    例如：[1,2,3] ---> 1 2 3 每个元素一行
"""


def ssk():
    list01 = [1, 2, 3, 4, 5, 6, 7]
    for x in list01:
        print(x)


ssk()


# 以上代码是把 函数写死了
def print_list(list_target):
    """
        打印列表
    :param list_target: 目标列表
    :return:
    """
    for x in list_target:
        print(x)


list02 = [11, 21, 32, 43, 54, 68, 7]
print_list(list02)
