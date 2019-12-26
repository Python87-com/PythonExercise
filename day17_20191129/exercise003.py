"""
    练习03：
        1、获取列表中所有字符串
        2、获取列表中所有小数
    要求：分别使用 生成器函数/生成器表达式/列表推导式
"""
list01 = [1, "3", 5, 7, 9.0, 5.23, True, 'OK', 5.2, 456, "孙悟空", 6.3, 20, "52"]

# 1、获取列表中所有字符串
# for item in list01:
#     if type(item) == str:
#         print(item)

# 推导式
str01 = [item for item in list01 if type(item) == str]
print(str01)
float01 = [item for item in list01 if type(item) == float]
print(float01)
# 生成器表达式
str02 = (item for item in list01 if type(item) == str)
for item in str02:
    print(item)
float02 = [item for item in list01 if type(item) == float]
for item in float02:
    print(item)


# 生成器函数
def str_find(iter_target):
    for item in iter_target:
        if type(item) == str:
            yield item


re = str_find(list01)
for item in re:
    print(item)


# 小数
def str_find2(iter_target):
    for item in iter_target:
        if type(item) == float:
            yield item


re2 = str_find2(list01)
for item in re2:
    print(item)
