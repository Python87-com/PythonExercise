"""
    练习4:
    在list_helper.py中增加通用的升序排列方法.
    案例1:将敌人列表按照攻击力进行升序排列.
    案例2:将敌人列表按照防御力进行升序排列.
    案例3:将敌人列表按照血量进行升序排列.
"""


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


# 升序
def find01():
    for x in range(len(list_enemy)):
        for y in range(len(list_enemy)):
            if list_enemy[x].attack < list_enemy[y].attack:
                list_enemy[x], list_enemy[y] = list_enemy[y], list_enemy[x]
def find02():
    for x in range(len(list_enemy) - 1):
        for y in range(x + 1, len(list_enemy)):
            if list_enemy[x].attack > list_enemy[y].attack:
                list_enemy[x], list_enemy[y] = list_enemy[y], list_enemy[x]
find02()
for item in list_enemy:
    print(item)
# for item in find01():
#     for x in item:
#         print(x)
