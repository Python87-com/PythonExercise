"""
    测试 通用模块list_helper

    # 练习:在list_helper.py中,定义通用的查找满足条件的单个对象.
    # 案例:查找名称是"葵花宝典"的技能.
    #     查找编号是101的技能.
    #     查找持续时间大于0的技能.

    # 建议:
    # 1. 现将所有功能实现
    # 2. 封装变化(将变化点单独定义为函数)
    #    定义不变的函数
    # 3. 将不变的函数转移到list_helper.py中
    # 4. 在当前模块测试
"""



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

from common.list_helper import *
# 变化点封装
# lamdba 练习

re = ListHelper.find_single(list_skill, lambda item: item.name == "葵花宝典")
print(re)

print("--------------------------")

re2 = ListHelper.find_single(list_skill, lambda item: item.id == 101)
print(re2)

print("--------------------------")

re3 = ListHelper.find_single(list_skill, lambda item: item.duration > 0)
print(re3)
