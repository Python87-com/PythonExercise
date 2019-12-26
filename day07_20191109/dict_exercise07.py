
money = int(input("请输入您的金额："))

if money < 1 or money > 10000000:
    print("你逗我玩呢？")
elif money >= 10000:
    print("国外玩去吧")
elif money >= 5000:
    print("去西藏玩吧")
elif money > 2000:
    print("去二线城市玩吧")
else:
    print("还是在家玩吧")