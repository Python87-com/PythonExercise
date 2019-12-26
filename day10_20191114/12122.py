"""
    删除列表中大于10的数字
"""
# list01 = [9, 25, 12, 8]
list01 = [5, 56, 6, 7, 7, 8, 19]
# list02 = []
# for i in list01:
#     list02.append(i +1)


list02 = [i + 1 for i in list01]
print(list02)
