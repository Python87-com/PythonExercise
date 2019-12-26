"""
    练习
    判断列表中元素是否具有相同的 [xxxxx]
    思路：所有元素两两比较，发现相同的则打印结果
        所有元素比较结束，都没有发现相同的，则打印结果
"""

list01 = [1, 3, 5, 1, 2, 9, 5]
# 做个标记
result = False
for x in range(len(list01) - 1):
    for y in range(x + 1, len(list01)):
        if list01[x] == list01[y]:
            print("具有相同的数据")  # 只需要显示一次，并没有要求把重复项打印出来
            result = True
            break  # 这个是退出内层循环
    if result:
        break  # 这个是退出外层循环
