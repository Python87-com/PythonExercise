"""
    列表推导式嵌套
"""
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = []
for i in list01:
    for k in list02:
        list03.append(i + k)

print(list03)

# 推导式
list04 = [i + k for i in list01 for k in list02]
print(list04)
