"""
    练习：定义生成器函数 my_enumerate ,实现下列现象
        将元素与索引合成一个元组
"""
list01 = [1, 9, 56, 12, 85, 4, 123]


# for item in enumerate(list01):
#     # （索引，元素）
#     print(item)
#
# for index, element in enumerate(list01):
#     # （索引，元素）
#     print(index, element)

def my_enumerate(iterable_target):
    # index = 0
    # for item in iterable_target:
    #     yield (index, item)
    #     index += 1

    for index in range(len(iterable_target)):
        yield index, iterable_target[index]


for index, element in my_enumerate(list01):
    print(index, element)


