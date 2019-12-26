


list01 = [      # 值  下标规律
    [1, 2, 3],  # 1    0 0
    [4, 5, 6],  # 5    1 1
    [7, 8, 9]]  # 9    2 2

# 取出 1 5 9
list02 = []
for i in range(len(list01)):
    list02.append(list01[i][i])

print(list02)

list03 = [list01[i][i] for i in range(len(list01))]

print(list03)
