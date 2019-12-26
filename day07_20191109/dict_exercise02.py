"""
    ["无忌","赵敏","周芷若"]
    房间号 [101,102,103]
"""
list_people = ["无忌", "赵敏", "周芷若"]
list_home_num = [101, 102, 103]
dict_people = {}
count = 0
# for item in list_people:
#     # 拿出的是名称
#     dict_people[item] = list_home_num[count]
#     count += 1
# print(dict_people)

for i in range(len(list_people)):
    dict_people[list_people[i]] = list_home_num[i]

print(dict_people)