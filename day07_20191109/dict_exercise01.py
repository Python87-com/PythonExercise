"""
    ["无忌","赵敏","周芷若"]
    存在字典里
    无忌 -- 2   赵敏  -- 2   周芷若 --3
"""
list_people = ["无忌","赵敏","周芷若"]
dict_people = {}
# 列表拿数据
for item in list_people:
    dict_people[item] = len(item)

print(dict_people)



