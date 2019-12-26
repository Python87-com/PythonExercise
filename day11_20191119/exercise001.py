"""
    创建一个敌人类 姓名、攻击力10-50、血量 100-200
    创建一个敌人对象，可以修改数据，读取数据
"""


class Enemy:

    def __init__(self, name, agg, hp):
        self.name = name
        # self.__agg = agg
        # self.__hp = hp
        self.set_agg(agg)
        self.set_hp(hp)

    def get_agg(self):
        return self.__agg

    def set_agg(self, value):
        if 10 <= value <= 50:
            self.__agg = value
        else:
            raise ValueError("攻击力输入错误（10 - 50)")

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("血量输入错误 (100 - 200)")


# 创建一个敌人对象
en01 = Enemy("铁扇公主", 35, 150)

# 访问数据   攻击力
en01.set_agg(45)
print(en01.get_agg())
# 访问数据   血量
en01.set_hp(145)
print(en01.get_hp())