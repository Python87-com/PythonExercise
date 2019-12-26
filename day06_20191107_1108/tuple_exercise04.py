"""
    在控制台录入日期（3月5日 格式如 3-5），计算是一年中的第几天
    1月的天数 + 2月的天数 + 5
"""
# 接收用户输入的数据
user_input = input("请输入日期：")
# 分割月日存储在 元组 或 列表 中
# user_date = user_input.split("-", 1) 默认分割成列表
user_date = tuple(user_input.split("-", 1))
print(type(user_date))
# ('3' , '5')
# 建立一个元组用于存储一年12个月，每个月的天数
month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# user_date 元组存储的数据是 字符串 类型，需要转换成可以计算的 int 类型
for_int = int(user_date[0])
days = 0
for i in range(for_int - 1):
    days += month_day[i]
# 打印的时候要注意 还有一个零头的天数 要加上去
print(days + int(user_date[1]))
