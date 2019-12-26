"""
定义 一个列表：内容为：湖人、热火、马刺     1.要求：加入James到第一个位置    2.删除热火元素    3 尾部追加  科比
"""

list01 = ["湖人", "热火", "马刺"]
print(list01)

# 1.要求：加入James到第一个位置
list01.insert(0, "James")
print(list01)

# 2.删除热火元素
for i in list01:
    if i == "热火":
        list01.remove(i)
print(list01)

# 3 尾部追加  科比
list01.append("科比")
print(list01)




