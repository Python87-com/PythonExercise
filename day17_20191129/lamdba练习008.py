"""
   # 需求1:计算技能列表中技能名称大于4个字的技能数量.
    # 需求2:计算技能列表中技能持续时间小于等于5的技能数量.
    # 步骤:
    # 实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    # 将不变的函数提取到list_helper.py中
"""
from common.list_helper import *


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

def find():
    count = 0
    for item in list_skill:
        if len(item.name) > 4:
            count += 1
        return count


# def find2():
#     count = 0
#     for item in list_skill:
#         if item.duration <= 5:
#             count += 1
#         return count

re = ListHelper.find_count(list_skill,lambda item:len(item.name) > 4)
print(re)
# print("--------------------------")
re2 = ListHelper.find_count(list_skill,lambda item:item.duration <= 5)
print(re2)

# 需求1:计算技能列表中技能名称大于4个字的技能数量.
# re = ListHelper.find_jn(list_skill,lambda item:len(item.name) > 4)
# for item in re:
#     print(item)
# print("--------------------------")
# # 需求2:计算技能列表中技能持续时间小于等于5的技能数量.
# re2 = ListHelper.find_jn(list_skill,lambda item:item.duration <= 5)
# for item in re2:
#     print(item)

# 变化点封装
# lamdba 练习

# def find():
#     for item in list_skill:
#         if len(item.name) > 4:
#             yield item
# def find2():
#     for item in list_skill:
#         if item.duration <= 5:
#             yield item
#
# def condition01(item):
#     return len(item.duration) <= 5

# re = ListHelper.find_single(list_skill, lambda item: item.name == "葵花宝典")
# print(re)
#
# print("--------------------------")
#
# re2 = ListHelper.find_single(list_skill, lambda item: item.id == 101)
# print(re2)
#
# print("--------------------------")
#
# re3 = ListHelper.find_single(list_skill, lambda item: item.duration > 0)
# print(re3)
