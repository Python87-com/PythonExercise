"""
    列表排序（升序 小--> 大）
"""
list01 = [10,5,99,15,3,58,63,4,1,75,32,26,8]
list02 = []
for x in range(len(list01) - 1):
    for y in range(x + 1, len(list01)):
        if list01[x] > list01[y]:
           list01[x], list01[y] = list01[y], list01[x]
print(list01)

# 降序
list01 = [10,5,99,15,3,58,63,4,1,75,32,26,8]
list02 = []
for x in range(len(list01) - 1):
    for y in range(x + 1, len(list01)):
        if list01[x] < list01[y]:
           list01[x], list01[y] = list01[y], list01[x]
print(list01)