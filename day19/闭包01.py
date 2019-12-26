"""
函数式编程  闭包
"""

# 下面的代码是一个连续的逻辑 闭包
def give_gife_money(money):
    print("得到%d元压岁钱" % money)

    def child_buy(target, price):
        nonlocal money
        if money >= price:
            money -= price
            print("孩子花了%.1f元钱，购买了%s." % (price, target))
        else:
            print("钱不够啦")
    return child_buy  # 将内部函数作为返回值

action = give_gife_money(10000)
action("唐僧肉",5)
action("小汽车",2000)
action("苹果手机",8000)