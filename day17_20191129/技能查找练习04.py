"""

"""


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    # 重写 str 方法
    def __str__(self):
        return "技能数据：%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
    SkillData(104, "十八罗汉棍", 3, 20)
]


# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成
def skill_find01():
    for item in list_skill:
        if item.atk_ratio > 6:
            print(item)


skill_find01()
print("--------------------------------------")
# 表达式
re01 = (item for item in list_skill if item.atk_ratio > 6)
for item in re01:
    print(item)
print("--------------------------------------")


# 练习2:获取持续时间在4--11之间的所有技能
def skill_find02():
    for item in list_skill:
        if 4 < item.duration < 11:
            print(item)


skill_find02()
print("--------------------------------------")
# 表达式
re02 = (item for item in list_skill if 4 < item.duration < 11)
for item in re02:
    print(item)
print("--------------------------------------")


# 练习3:获取技能编号是102的技能
def skill_find03():
    for item in list_skill:
        if item.id == 102:
            return item


print(skill_find03())
print("----------------3----------------------")


# 练习4:获取技能名称大于4个字并且持续时间小于6的所有技能
def skill_find04():
    for item in list_skill:
        if len(item.name) >= 4 and item.duration < 6:
            yield item


s01 = skill_find04()
for item in s01:
    print(item)

"""
技能数据：102,降龙十八掌,8,5
技能数据：103,葵花宝典,10,2
--------------------------------------
技能数据：102,降龙十八掌,8,5
技能数据：103,葵花宝典,10,2
--------------------------------------
技能数据：101,乾坤大挪移,5,10
技能数据：102,降龙十八掌,8,5
--------------------------------------
技能数据：101,乾坤大挪移,5,10
技能数据：102,降龙十八掌,8,5
--------------------------------------
技能数据：102,降龙十八掌,8,5
----------------3----------------------
技能数据：102,降龙十八掌,8,5
技能数据：103,葵花宝典,10,2
"""