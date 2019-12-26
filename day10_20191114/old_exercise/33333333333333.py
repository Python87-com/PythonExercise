"""
    编写函数，接收字符串参数，返回一个元组，其中第一个元组为大写字母的个数，第二个元素为小写字母的个数
    例如：print(demo2("AAAAAAAAAAzzxxxxxxxxxx"))
    结果：(10, 12)
"""


def demo2(str_input):
    result = [0, 0]
    for i in str_input:
        if 'a' <= i <= 'z':
            result[1] += 1
        elif 'A' <= i <= 'Z':
            result[0] += 1
    return tuple(result)


print(demo2("AAAAAAAAAAzzxxxxxxxxxx"))

str_input = "AAAAAAA21AAAzzx2xxxx34x5xxxx"
#         大  小
list02 = [0, 0]

for item in str_input:
    if item.isupper():
        list02[0] += 1
    elif item.islower():
        list02[1] += 1

print(list02)