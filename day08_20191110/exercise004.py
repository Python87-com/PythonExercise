"""
    练习 定义 判断列表中是否存在相同元素的 函数
list01 = [1,3,5,1,2,9,5]
# 做个标记
result = False
for x in range(len(list01) - 1):
    for y in range(x + 1, len(list01)):
        if list01[x] == list01[y]:
            print("具有相同的数据")    # 只需要显示一次，并没有要求把重复项打印出来
            result = True
            break       # 这个是退出内层循环
    if result:
        break   # 这个是退出外层循环
"""
# def judge_same_number(list_num):
#     """
#         判断列表中是否存在相同元素
#     :param list_num: 列表
#     :return: 返回结果 str
#     """
#     for x in range(len(list_num) - 1):
#         for y in range(x + 1, len(list_num)):
#             if list_num[x] == list_num[y]:
#                 return "具有相同的数据"    # 只需要显示一次，并没有要求把重复项打印出来
#     return "没有相同的数据"

# 2种选择的时候 建议使用bool
def judge_same_number(list_num):
    """
        判断列表中是否存在相同元素
    :param list_num: 目标列表
    :return: 返回结果 bool True 有相同
    """
    for x in range(len(list_num) - 1):
        for y in range(x + 1, len(list_num)):
            if list_num[x] == list_num[y]:
                return True    # 只需要显示一次，并没有要求把重复项打印出来
    return False

list01 = [1, 3, 5, 1, 2, 9, 5]

print(judge_same_number(list01))