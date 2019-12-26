"""
    列表推导式嵌套
"""
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
# cc = []
# for r in list01:
#     for c in list02:
#         cc.append(r + c)
#
# print(cc)
# 推导式
d = [r + c for r in list01 for c in list02]
print(d)
