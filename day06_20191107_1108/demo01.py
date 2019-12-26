"""
    老师的代码
"""
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int("请输入月份：")
day = int("请输入日：")

# 累加前几个月天数
total_day = 0
for i in range(month - 1):
    total_day += day_of_month[i]

# 累加当月天数
total_day += day

print("是这年的第%d天。" % (total_day))

# 方法二 切片的方式
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int("请输入月份：")
day = int("请输入日：")
# 切片取出来的还是元组，使用sum函数求和
total_day = sum(day_of_month[:month - 1])
# 总天数  继续累加
total_day += day
print("是这年的第%d天。" % (total_day))
