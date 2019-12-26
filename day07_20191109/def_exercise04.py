"""
3. 定义在控制台中打印二维列表的函数
[
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]
"""
list01 = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]


# 定义一个函数
def print_list(list_target):
    """
        打印二维列表
    :param list_target: 目标列表
    :return:
    """
    for x in range(len(list_target)):
        for y in list_target[x]:
            print(y, end=" ")
        print()


# 打印
print_list(list01)
