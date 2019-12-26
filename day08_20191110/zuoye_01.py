"""
3. 自学(参照菜鸟教程)字符串/列表/字典常用函数(方法),实现如下功能。
    字符串："　校　训：自　强不息、厚德载物。　　"
    查找空格的数量
    删除字符串前后空格
    删除字符串所有空格
    查找"载物"的位置
    判断字符串是否以"校训"开头.
"""
str01 = " 校 训：自 强不息、厚德载物。  "

# 判断字符串长度
print(len(str01))  # 18

# 查找空格的数量
print(str01.count(" "))  # 5

# 删除字符串前后空格
# 删除左侧空格
str02 = str01.lstrip()
# 删除右侧空格
str03 = str02.rstrip()
print(str02)
print(str03)

# 也可以合并删除   str02 = str01.lstrip().rstrip()

# 删除字符串所有空格
str04 = str01.replace(" ", "")
print(str04)

# 查找"载物"的位置
# 返回的是索引，如要位置则 + 1
print(str01.index("载物"))

# 判断字符串是否以"校训"开头.
print(str01.startswith("校训"))   # False
print(str04.startswith("校训"))   # True