"""
    推导式
    使用range生成1--10之间的数字，将数字的平方list01中
"""
# print("您好")

num = range(1, 10)
list01 = []

for item in range(1, 11):
    list01.append(item ** 2)
print(list01)

# 推导式
list02 = [item ** 2 for item in range(1, 11)]
print(list02)