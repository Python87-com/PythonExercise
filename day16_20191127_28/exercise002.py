"""
    面试题：不使用 for 循环，获取字典内所有元素

    {"铁扇公主"：101,"铁锤公主":102,"扳手王子":103}

"""
dict01 = {"铁扇公主1": 101, "铁锤公主2": 102, "扳手王子3": 103}

# 1获取迭代器
d_iter = dict01.__iter__()

# 2循环获取下一个元素
while True:
    try:
        # 获取下一个元素 获取的是key  【value？ dict01[key]  -- > valule】
        key = d_iter.__next__()
        print(key, dict01[key])
    # 3遇到异常停止迭代
    except StopIteration:
        break
