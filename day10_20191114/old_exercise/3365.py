"""
    编写函数 接收 包含20个整数的列表lst和一个整数k作为参数，返回新列表。
    处理规则：将列表lst中下标k之前的元素逆序，下标k之后的元素逆序，然后将整个列表lst中的所有元素逆序。
"""
lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

list01 = []


def demo3(lst, k):
    for i in range(-1, -len(lst) + k, -1):
        list01.append(lst[i])
    return list01


demo3(lst, 10)
print(list01)
# [39, 37, 35, 33, 31, 29, 27, 25, 23]

list02 = []


def demo4(lst, k):
    for i in range(-10 - 1, -len(lst) - 1, -1):
        list02.append(lst[i])
    return list02


demo4(lst, 10)
print(list02)
# [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

list03 = []


def demo5(lst):
    for i in range(-1, -len(lst) - 1, -1):
        list03.append(lst[i])
    return list03


demo5(lst)
print(list03)


# [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]


def demo66(lst, k):
    x = lst[:k]
    x.reverse()
    y = lst[k:]
    y.reverse()

    r = x + y

    return list(reversed(r))


lst = list(range(1, 21))

print(lst)

print(demo66(lst, 5))


# ------------------运行效率比上面 66 的速度快
def demo77(lst, k):
    temp = lst[:]
    for i in range(k):
        temp.append(temp.pop(0))
    return temp


print(demo77(lst, 5))

print("*" * 20)


# 使用切片操作
def demo88(lst, k):
    return lst[k:] + lst[:k]


print(demo88(lst, 5))
