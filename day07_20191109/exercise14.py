"""
    练习：列表的全排列
    ["香蕉","苹果","哈密瓜"]
    ["可乐","牛奶"]
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["可乐", "牛奶"]

list03 = []

for x in list01:
    for y in list02:
        list03.append(x + y)

print(list03)

list04 = [x + y for x in list01 for y in list02]
print(list04)



