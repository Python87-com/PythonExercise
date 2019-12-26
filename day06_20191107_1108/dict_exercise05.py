"""
    在控制台中循环录入商品信息（名称，单价）
    如果名称输入空字符串，则停止录入
    将所有信息逐行打印出来
"""
shop = {}
while True:
    shop_name = input("请输入商品名称：")
    if shop_name == "":
        break
    shop_price = input("请输入商品单价：")
    shop[shop_name] = shop_price

# 打印
for k, v in shop.items():
    print(k, v)