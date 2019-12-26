"""
    将list01中 所有奇数存入list02
    将list01中 所有偶数存入lsit03
    将list01中 所有偶数大于5的数字+1后存入 list04
    list01 = [item ** 2 for item in range(1, 10)]
"""
list01 = [item ** 2 for item in range(1, 11)]
print(list01)
# 将list01中所有奇数存入list02
# list02 = []
# list03 = []
# list04 = []
# for item in list01:
#     if item % 2 == 1:
#         list02.append(item)
list02 = [item for item in list01 if item % 2 == 1]
print(list02)
# 将list01中所有偶数存入lsit03
# for item in list01:
#     if item % 2 == 0:
#         list03.append(item)
list03 = [item for item in list01 if item % 2 == 0]
print(list03)

# 将list01中所有偶数大于5的数字 + 1后存入list04
# for item in list01:
#     if item % 2 == 0 and item > 5:
#         list04.append(item + 1)
list04 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]
print(list04)

