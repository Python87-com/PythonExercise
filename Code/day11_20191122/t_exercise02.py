"""
    请为如下万年历程序进行自顶向下设计，画出模块图，并实现之。它的功能是：
    用户输入某年、某月、某日，程序输出这一天是星期几；
    用户输入某年、某月,程序输出该年该月的每一天是星期几
    用户输入某年，程序输出该年每一月的每天是星期几。
    该程序的求解方案是：为给定的年、月、日计算它距离1900年1月1日（星期一）
    的天数，从而得出星期几（注意考虑间隔年为闰年的情况）
"""


# 2019.11.22 周五
class Calendar:


    def __init__(self, year=1990, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    # 判断闰年
    def judgement_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return 1
        return 0

    # 计算1900年1月1日到用户输入的日期总共多少天
    def calculation_year(self):
        global result_days
        result_days = 0
        global re_year
        for item in range(1990, self.year):
            # 判断闰年
            re_year = Calendar.judgement_leap_year(self)
            if re_year:
                result_days += 366
            else:
                result_days += 365
            # print(result_days)
        return result_days

    # 计算月份的天数  例如 7月  前6个月的天数 + 日数
    def calculation_month(self):
        global re_days
        re_days = 0
        list_year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month in range(self.month - 1):
            re_days += list_year_days[month]
        if re_year:
            re_days += 1
        # print(re_days)
        return re_days

    # 计算周几
    def calculation_week(self):
        # 计算周几  1990.1.1 周一
        # 总天数 * 7     2019.7.3   184 % 7 = 2 周三
        list_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
        Calendar.calculation_year(self)
        Calendar.calculation_month(self)
        result = 0
        result = result_days + re_days + self.day
        # week = list_week[result % 7 - 1]
        week = result % 7
        return week


# 调用日历 输入年月日显示星期几
s1 = Calendar(2019, 7, 3)
print(s1.calculation_week())