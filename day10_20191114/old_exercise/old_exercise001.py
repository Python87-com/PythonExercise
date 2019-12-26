"""
    矩阵转置
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

list01 = [
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
]
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# 0 0 - 1 0 - 2 0 - 3 0
# 0 1 - 1 1 - 2 1 - 3 1
# 0 2 - 1 2 - 2 2 - 3 2
# 0 3 - 1 3 - 2 3 - 3 3

list02 = []
# for r in range(len(list01)):  # 0 1 2 3
#     line = []
#     list02.append(line)
#     for c in range(len(list01)):  # 0 1 2 3
#         line.append(list01[c][r])

for r in range(len(list01)):  # 0 1 2 3
    list02.append([])
    for c in range(len(list01)):  # 0 1 2 3
        list02[r].append(list01[c][r])

print(list02)
