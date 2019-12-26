"""
    定义父类
        车（数据：品牌，速度）
    定义子类
        电动车（数据：电池容量，充电功率）
"""


class Car(object):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def say(self):
        print("品牌是：", self.brand, "速度是：", self.speed)


class ElectricVehicle(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        """

        :param brand:
        :param speed:
        :param battery_capacity:
        :param charging_power:
        """
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

    def run(self):
        print("品牌是：", self.brand, "速度是：", self.speed, "电池容量", self.battery_capacity, "充电功率", self.charging_power)


c01 = Car("雅迪", 180)
# 父类只能调用父类的方法
c01.say()
# c01.run() # 报错 AttributeError: 'Car' object has no attribute 'run'  attributeRor:“Car”对象没有“run”属性
e01 = ElectricVehicle("松江", 150, 250, 95)
# 子类可以调用子类方法
e01.run()
# 子类可以调用父类的方法
e01.say()