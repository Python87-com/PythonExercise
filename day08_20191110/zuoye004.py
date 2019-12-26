"""
    重构 shopping.py 程序
   不改变原有功能，修改程序代码。
"""
# 商品总价的全局变量total_shopping_price
total_price = 0

# 商品列表 字典
dict_product_list = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

# 订单
# 创建一个订单列表 用于存储用户购买商品的列表
list_order = []


# 定义一个 商品购买 的 函数 Shopping
def shopping_purchase():
    for key, value in dict_product_list.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_product_list:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    list_order.append({"cid": cid, "count": count})
    print("添加到购物车。")
    shopping()


# 定义一个用于 商品结算 的函数
def shopping_settlement():
    global total_price
    total_price = 0
    for item in list_order:
        commodity = dict_product_list[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
        total_price += commodity["price"] * item["count"]
    while True:
        # 付款金额判断 payment_amount
        payment_amount = float(input("商品总价 %d 元，请输入付款金额：" % (total_price)))
        if payment_amount >= total_price:
            print("商品购买成功，找您：%d 元。" % (payment_amount - total_price))
            # 清空购物车，以便下次购买
            list_order.clear()
            break
        else:
            print("您支付的金额不足.")
    shopping()


# 定义一个 购物 函数
def shopping():
    user_input = input("1键购买，2键结算。")
    # 对用户的行为处理
    user_behavior(user_input)


# 定义一个判断 用户行为 的函数
def user_behavior(user_input):
    if user_input == "1":
        # 商品采购
        shopping_purchase()
    if user_input == "2":
        # 商品结算
        shopping_settlement()
    return "如果你不是来购物的,还请去其他地方看看吧！"


# 开始购物
shopping()
