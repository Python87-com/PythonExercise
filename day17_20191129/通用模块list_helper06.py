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


# 变化点封装
def condition01(item):
    return item.name == "葵花宝典"


def condition02(item):
    return item.id == 101


def condition03(item):
    return item.duration > 0


# 继承
# def find(func):
#     for item in list_skill:
#         # 多态
#         if func(item):
#             return item
#
# print(find(condition01))
re = ListHelper.find_single(list_skill,condition03)
print(re)

# 案例:查找名称是"葵花宝典"的技能.
# def find01():
#     for item in list_skill:
#         if item.name == "葵花宝典":
#             return item


# re = find01()
# print(re)
# print(find01())
print("-------------2---------------------")


#     查找编号是101的技能.
# def find02():
#     for item in list_skill:
#         if item.id == 101:
#             return item
#
#
# print(find02())
print("------------3----------------------")


#     查找持续时间大于0的技能.
# def find03():
#     for item in list_skill:
#         if item.duration > 0:
#             return item
#
#
# print(find03())
