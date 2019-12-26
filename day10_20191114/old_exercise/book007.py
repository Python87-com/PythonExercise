"""
    输出序列中的元素
"""
list01 = ['a', 'b', 'mpilgrim', 'z', 'example']
for i, v in enumerate(list01):
    print("列表的第", i + 1, "个元素是：", v)

list02 = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(list02)):
    print(i)  # 这个打出的是 index 索引值

for i in range(len(list02)):
    print(list02[i], end=" ")

print()

for item in list02:
    print(item, end=" ")
print()

for i in range(-1, -len(list02) - 1, -1):
    print(list02[i], end=" ")
