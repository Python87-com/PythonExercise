"""
   不使用for循环获取元组内所有元素
    ("铁扇公主","铁锤公主","扳手王子")
"""

tuple01 = ("铁扇公主","铁锤公主","扳手王子")

# 获取迭代器
item = tuple01.__iter__()
while True:
    try:
        i = item.__next__()
        print(i)
    except StopIteration:
        break
