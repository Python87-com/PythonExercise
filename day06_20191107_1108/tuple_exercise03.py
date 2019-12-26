"""
    借助元组完成下列功能
# 获取月份
month = int(input("请输入月份："))
# 逻辑
if month < 1 or month > 12:
    print("输入有误。")
elif month == 2:
    print("28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
else:
    print("31天")
"""
month = int(input("请输入月份："))

# 建立一个元组把30天的月份都存储起来
tuple30 = (4, 6, 9, 11)
if month < 1 or month > 12:
    print("输入有误。")
elif month == 2:
    print("28天")
elif month in tuple30:
    print("30天")
else:
    print("31天")

# ******************************************************
# 方法二
month = int(input("请输入月份："))
# 建立一个元组，将一年12个月每个月的天数存储起来
month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

if month < 1 or month > 12:
    print("输入有误。")
else:
    print("{0}天".format(month_day[month - 1]))
