"""
    类变量
"""


class ICBC:
    # 类变量  总行的钱
    total_money = 5000000

    def __init__(self, name, money):
        self.name = name
        self.money = money
        ICBC.total_money -= money


# 创建银行支行
bank01 = ICBC("工商银行六合支行", 2500000)
bank02 = ICBC("工商银行浦口支行", 1500000)

# 总行的钱还剩余多少
print(ICBC.total_money)     # 100 0000
