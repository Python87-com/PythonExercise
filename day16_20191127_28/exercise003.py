"""
    练习1：从列表中选出所有偶数 [21,55,65,22,99,88,12,44,66]
    2种方法实现   1、存入一个新的列表
    2、使用生成器实现
"""
list01 = [21, 55, 65, 22, 99, 88, 12, 44, 66]

list02 = []


# for item in list01:
#     if item % 2 == 0:
#         list02.append(item)


# [22, 88, 12, 44, 66]
# print(list02)

def my_list01():
    result = []
    for item2 in list01:
        if item2 % 2 == 0:
            result.append(item2)
    return result


l01 = my_list01()
for item in l01:
    print(item, end=" ")

print()


# 生成器
def my_list02():
    for item in list01:
        if item % 2 == 0:
            yield item


re = my_list02()
for item in re:
    print(item)
