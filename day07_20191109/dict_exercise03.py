"""
    需求：字典如何根据 value 查找 key
"""
dict01 = {'无忌': 101, '赵敏': 102, '周芷若': 103}

# 解决方案一
# 缺点：如果 key 重复，交换后则数据会丢失
dict02 = {value: key for key, value in dict01.items()}

# 解决方案二  列表里面套元组
# [(k,v),(k,v)]
list01 = [(key, value) for key, value in dict01.items()]

print(list01)
# [('无忌', 101), ('赵敏', 102), ('周芷若', 103)]