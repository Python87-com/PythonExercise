"""
[1,5,9,13]
[2,6,10,14]
[3,7,11,15]
[4,8,12,16]
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
list02 = []
for i in range(len(list01)):  # 行索引
    line = []
    list02.append(line)
    for k in range(len(list01)):  # 列索引
        # print(list01[k][i], end = " ")
        # 遍历得到4个数，存入到一个列表中
        line.append(list01[k][i])

print(list02)

# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
