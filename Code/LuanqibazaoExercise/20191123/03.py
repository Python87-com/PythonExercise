# 使用方法，封装变量.
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.__age = age
        self.__weight = weight


w01 = Wife("铁锤公主", 87, 87)
# 重新创建了新实例变量(没有改变类中定义的__age)
# w01.__age = 107　
w01._Wife__age = 107  # (修改了类中定义的私有变量)
print(w01.__dict__)  # python内置变量,存储对象的实例变量.
# w01 = Wife("铁锤公主", 30, 50)
# w01.set_age(25)
# w01.set_weight(55)
# print(w01.get_age())
# print(w01.get_weight())
