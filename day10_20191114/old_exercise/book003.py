"""
    使得list01列表 平铺在一个新的列表中
    如：list01 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    变成：[1, 2, 3, 4, 5, 6, 7, 8, 9]
    使用循环和列表推导式完成
"""
list01 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list02 = []
for item in list01:
    for num in item:
        list02.append(num)

print(list02)


# 推导式实现列表元素平铺在一个列表中

list03 = [num for item in list01 for num in item]

print(list03)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]