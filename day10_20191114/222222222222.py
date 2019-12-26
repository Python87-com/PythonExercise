"""
    编写函数，接收任意多个实数，返回一个元组，其中第一个元素为所有参数的平均值，其他元素为所有参数中大于平均数的实数。
    例如：demo(25,36,99,108,16,22,5,9,23)
    结果：(38.111111111111114, 99, 108)
"""


# def demo(*para):
#     avg = sum(para)/len(para)
#     g = [i for i in para if i > avg]
#     return (avg,) + tuple(g)
#
#
#
# print(demo(25,36,99,108,16,22,5,9,23))


def demo1(*para):
    # 计算平均值
    average_value = sum(para) / len(para)

    # 创建一个空列表，存储下列计算后的数据
    list01 = []

    for i in para:
        if i > average_value:
            list01.append(i)
    return (average_value,) + tuple(list01)


print(demo1(25,36,99,108,16,22,5,9,23))


元组合并
a = (22,)
c = [1, 3, 5, 7, 9]
b = tuple(c)
print(a + b)
