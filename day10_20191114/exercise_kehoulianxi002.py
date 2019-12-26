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


# 查找姓名是“灭霸”的敌人对象
def find01():
    for item in list_en_info:
        if item.name == "灭霸":
            return item


en01 = find01()
en01.print_info()  # 灭霸 50000 10000 5600


# 查找所有死亡的敌人
def find02():
    en_info = []
    for item in list_en_info:
        if item.HP == 0:
            en_info.append(item)
    return en_info


en02 = find02()
for item in en02:
    item.print_info()
"""
祖玛雕像 0 200 100
祖玛弓箭手 0 300 200
祖玛卫士 0 200 300
魔龙血兵 0 300 500
魔龙刀卫 0 400 900
"""


# 计算所有敌人的平均攻击力
def find03():
    total_basic_attack = 0
    for i in range(len(list_en_info)):
        total_basic_attack += list_en_info[i].basic_attack
    return total_basic_attack / len(list_en_info)


print("所有敌人的平均攻击力:{0}".format(find03()))  # 2933.3333333333335


# 删除防御力小于1000的敌人
def del_enemy():
    # for item in list_en_info:
    #     if item.defense < 1000:
    #         print(item.defense)
    #         del item
    # return list_en_info
    for i in range(len(list_en_info)):
        if list_en_info[i].defense < 1000:
            print(list_en_info[i])
            del list_en_info[i]
    return list_en_info

del_enemy()
del_en = del_enemy()

# for item in del_en:
#     item.print_info()


# 将所有敌人攻击力增加5000

def add_enemy():
    for item in list_en_info:
        item.basic_attack += 5000
