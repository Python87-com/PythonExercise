"""
    方阵转置算法
    1  2  3  4    1  5 9  13
    5  6  7  8    2  6 10 14
    9  10 11 12   3  7 11 15
    13 14 15 16   4  8 12 16
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for x in range(len(list01)):
    for y in range(len(list01)):
        print(list01[y][x],end = " ")