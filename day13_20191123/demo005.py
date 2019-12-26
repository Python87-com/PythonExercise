"""
    手雷炸了，可能伤害敌人/玩家的生命.
             还可能伤害未知事物(鸭子.房子....)
    要求：增加了新事物，不影响手雷。
    体会：继承的作用
         多态的体现
         设计原则
            开闭原则
            单一职责
            依赖倒置
    画出设计图
    15:35
"""


# 定义一个手雷类
class Grenade:
    # 定义手雷的攻击力
    def __init__(self, atk):
        self.atk = atk

    def explode(self, damage_targe):
        print("手雷爆炸了")
        if not isinstance(damage_targe,Damageable):
            raise ValueError("不是Damageable的子类")
        damage_targe.damage(self.atk)


# 定义一个可以受伤的 父类
class Damageable:

    def damage(self, value):
        pass


# _________________________________________________________________
# 定义玩家类
class Player(Damageable):
    # 玩家血量
    def __init__(self, hp):
        self.hp = hp

    # 玩家受伤行为
    def damage(self, value):
        print("玩家受伤了")
        print("玩家血量减少")


# 定义一个敌人类
class Enemy(Damageable):
    # 敌人血量
    def __init__(self, hp):
        self.hp = hp

    # 敌人受伤行为
    def damage(self, value):
        print("敌人受伤了")
        print("敌人血量减少")


#______________________________________________
# 测试
# 手雷 攻击力 500
g01 = Grenade(500)

# 玩家 血量 200
p01 = Player(200)

g01.explode(p01)

"""
手雷爆炸了
玩家受伤了
玩家血量减少
"""