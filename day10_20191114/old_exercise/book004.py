"""
    将list01中所有大于0的数字提取出来存在一个新的列表中
    list01 = [-1,-4,6,7.3,-2.3,9,11]
"""
list01 = [-1, -4, 6, 7.3, -2.3, 9, 11]
list02 = []
for i in list01:
    if i > 0:
       list02.append(i)

print(list02)

# 列表推导式
list03 = [i for i in list01 if i > 0]

print(list03)