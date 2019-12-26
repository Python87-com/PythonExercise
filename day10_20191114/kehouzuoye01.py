"""
    定义敌人类 2019.11.14 23:10
        ----数据：姓名、血量、基础攻击力、防御力
        ----行为：打印个人信息

    创建敌人列表（至少4个元素），并画出内存图
    查找姓名是“灭霸”的敌人对象
    查找所有死亡的敌人
    计算所有敌人的平均攻击力
    删除防御力小于1000的敌人
    将所有敌人攻击力增加5000
"""


class Enemy:
    def __init__(self, name, HP, basic_attack, defense):
        self.name = name
        self.HP = HP
        self.basic_attack = basic_attack
        self.defense = defense

    def print_info(self):
        print(self.name, self.HP, self.basic_attack, self.defense)


# 创建敌人
list_en_info = [
    Enemy("灭霸", 50000, 10000, 5600),
    Enemy("沃玛教主", 10000, 2000, 1600),
    Enemy("魔龙守卫", 20000, 5000, 2600),
    Enemy("雪域神龙", 30000, 8000, 3600),
    Enemy("祖玛雕像", 0, 200, 100),
    Enemy("祖玛弓箭手", 0, 300, 200),
    Enemy("祖玛卫士", 0, 200, 300),
    Enemy("魔龙血兵", 0, 300, 500),
    Enemy("魔龙刀卫", 0, 400, 900),
]


# 删除防御力小于1000的敌人
def del_enemy():
    list_eny = []

    # 方法1 以下注释代码 运行通过
    # for item in list_en_info:
    #     if item.defense < 1000:
    #         # print(item.defense)
    #         del item
    #     else:
    #         list_eny.append(item)
    # return list_eny

    # 方法2  列表从后往前查找  找到并删除，不是则存入新的列表
    # for i in range(-1, -len(list_en_info), -1):  这样写  报错 IndexError: list index out of range
    for i in range(-len(list_en_info), -1):
        if list_en_info[i].defense < 1000:
            # print(list_en_info[i])
            del list_en_info[i]
        else:
            list_eny.append(list_en_info[i])
    return list_eny


# del_enemy()
del_en = del_enemy()

for item in del_en:
    item.print_info()


# 将所有敌人攻击力增加5000

def add_enemy():
    for item in list_en_info:
        item.basic_attack += 5000
    return list_en_info


add_en01 = add_enemy()

for item in add_en01:
    item.print_info()
