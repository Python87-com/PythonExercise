"""
    练习2:
    在list_helper.py中增加通用的筛选方法.
    案例1:获取敌人列表中所有敌人的名称.
    案例2:计算敌人列表中所有敌人的攻击力.
    案例3:计算敌人列表中所有敌人的名称和血量.
"""


# 以下代码一切以简洁练习目的，所有变量均公开


class Enemy:
    #                  姓名, 攻击力,防御力,血量
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp

    # 重写 __str__
    def __str__(self):
        return "{0}.攻击力{1},防御力{2},血量{3}".format(self.name, self.attack, self.defense, self.hp)


#  姓名, 攻击力,防御力,血量
list_enemy = [
    Enemy("灭霸", 500, 2000, 500),
    Enemy("祖玛卫士", 100, 500, 0),
    Enemy("沃玛教主", 300, 1000, 0),
    Enemy("雪原收割者", 400, 1500, 300),
    Enemy("触龙神", 200, 900, 0),
    Enemy("成昆", 200, 900, 10)
]


def find():
    for item in list_enemy:
        yield item.name
re = find()
for item in re:
    print(item)

def find2():
    for item in list_enemy:
        yield item.attack


def find3():
    for item in list_enemy:
        yield item.name, item.hp
