"""
    函数传参
        实际参数
"""


def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 位置参数：实参与形参根据位置进制依次对应
fun01(1, 2, 3, 4)

# 关键字实参：实参与形参根据名称进行对应
fun01(d=2, c=5, a=6, b=9)

# 序列实参：*号将序列拆分后按位置与形参进行对应
list01 = ["a", "b", "c", "d"]
# fun01(list01)
# TypeError: fun01() missing 3 required positional arguments: 'b', 'c', and 'd'

fun01(*list01)

# 字典实参：双*号将字典拆分后按名称与形参进行对应
# dict01 = {"a": 1, "b1": 2, "d": 5, "c": 9}
# dict01 = {"a": 1, "b": 2, "d": 5, "c": 9,"f":11}
dict01 = {"a": 1, "b": 2, "d": 5, "c": 9}
fun01(**dict01)

# TypeError: fun01() got an unexpected keyword argument 'b1'
# TypeError: fun01() got an unexpected keyword argument 'f'
print("*" * 25)

# 字符串
str01 = "1257"
fun01(*str01)

print("*" * 25)

# 元组
tuple01 = (5, 9, 15, 85)
fun01(*tuple01)
