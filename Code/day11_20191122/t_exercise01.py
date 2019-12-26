"""
    请为如下万年历程序进行自顶向下设计，画出模块图，并实现之。它的功能是：
    用户输入某年、某月、某日，程序输出这一天是星期几；
    用户输入某年，程序输出该年每一月的每天是星期几。
    该程序的求解方案是：为给定的年、月、日计算它距离1900年1月1日（星期一）
    的天数，从而得出星期几（注意考虑间隔年为闰年的情况）
"""

# 2019.11.22 周五

# class Calendar(object):
#     def __index__(self, year=1900, month=1, day=1):
#         self.year = year
#         self.month = month
#         self.day = day

# 判断闰年
# 平年28天、闰年29天
# 闰年共有366天(1-12月分别为31天,29天,31天,30天,31天,30天,31天,31天,30天,31天,30天,31天）
#
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))


# 判断闰年
def judgement_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1
    return 0


# 计算1900年1月1日到用户输入的日期总共多少天
def calculation_year(year):
    global result_days
    result_days = 0
    for year in range(1990, year):
        re_year = judgement_leap_year(year)
        if re_year:
            result_days += 366
        else:
            result_days += 365
        # print(result_days)
    return result_days


# 计算月份的天数  例如 7月  前6个月的天数 + 日数
def calculation_month(month):
    re_year = judgement_leap_year(year)
    global re_days
    re_days = 0
    list_year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(month - 1):
        re_days += list_year_days[month]
    if re_year:
        re_days += 1
    # print(re_days)
    return re_days


# 计算周几
def calculation_week(year, month, day):
    # 计算周几  1990.1.1 周一
    # 总天数 * 7     2019.7.3   184 % 7 = 2 周三
    list_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    calculation_year(year)
    calculation_month(month)
    result = 0
    result = result_days + re_days + day
    week = list_week[result % 7 - 1]
    print(week)


# 测试年
# calculation_year(year)  # 1990-2019  10592天
# calculation_month(month)
calculation_week(year, month, day)
