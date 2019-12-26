"""
    重构 shopping.py 程序
   不改变原有功能，修改程序代码。
"""
# 商品总价的全局变量
total_price = 0

# 商品列表
product_list = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

# 订单
# 创建一个订单列表 用于存储用户购买商品的列表
order_list = []


# 定义一个 商品购买 的 函数 Shopping
def shopping_purchase():
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            for key, value in product_list.items():
                print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
            while True:
                cid = int(input("请输入商品编号："))
                if cid in product_list:
                    break
                else:
                    print("该商品不存在")
            count = int(input("请输入购买数量："))
            order_list.append({"cid": cid, "count": count})
            print("添加到购物车。")
        elif item == "2":
            zong_jia = 0
            for item in order_list:
                shang_pin = product_list[item["cid"]]
                print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
                zong_jia += shang_pin["price"] * item["count"]
            while True:
                qian = float(input("总价%d元，请输入金额：" % zong_jia))
                if qian >= zong_jia:
                    print("购买成功，找回：%d元。" % (qian - zong_jia))
                    order_list.clear()
                    break
                else:
                    print("金额不足.")


# 定义一个用于 商品结算 的函数
def shopping_settlement():
    pass


# 定义一个 购物 函数
def shopping():
    # item = input("1键购买，2键结算。")
    user_input = input("1键购买，2键结算。")
    # 对用户的行为进行判断
    user_behavior(user_input)


# 定义一个判断用户行为的函数
def user_behavior(user_input):
    if user_input == 1:
        shopping_purchase()
    elif user_input == 2:
        shopping_settlement()


# 开始购物
shopping()
