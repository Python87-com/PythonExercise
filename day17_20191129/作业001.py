"""
3. 定义敌人类(姓名,攻击力,防御力,血量)
   创建敌人列表,使用list_helper实现下列功能.
   (1) 查找姓名是"灭霸"的敌人
   (2) 查找攻击力大于10的所有敌人
   (3) 查找活的敌人数量
"""
from common.list_helper import *


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
]

# (1) 查找姓名是"灭霸"的敌人

f01 = lambda item: item.name == "灭霸"
print(ListHelper.find_single(list_enemy, f01))
print("-------------------------------------------------")
# (2) 查找攻击力大于200的所有敌人
f02 = lambda item: item.attack > 200
e02 = ListHelper.find_all(list_enemy, f02)
for item in e02:
    print(item)
print("-------------------------------------------------")
# (3) 查找活的敌人数量
f03 = lambda item: item.hp > 0
e03 = ListHelper.find_all(list_enemy, f03)
for item in e03:
    print(item)
