"""
4. 在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
   案例1:判断敌人列表中是否存在"成昆"
   案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
    步骤:
    实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    将不变的函数提取到list_helper.py中
    体会：函数式编程的思想("封装，继承，多态")
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
    Enemy("成昆", 200, 900, 10)
]


# 思路
# 案例1: 判断敌人列表中是否存在"成昆"

def find1():
    for item in list_enemy:
        if item.name == "成昆":
            print(item)
            return True
    return False


# 案例2:, defense 判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
def find2():
    for item in list_enemy:
        if item.attack < 5 or item.defense < 10:
            return True
    return False
