"""
练习：定义函数 根据年月，计算有多少天，考虑闰年
    在控制台中获取月份
    打印天数  输入有误
    1 3 5 7 8 10 12 ---> 31天
    4 6 9 11 ---> 30天
    2   ---> 28天    闰年 29天

"""
# 判断是否是闰年的函数
def is_leap_year(year):
    """
        判断一个年份是否是闰年
    :param year: 目标年份
    :return: bool
    """
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    # 以上代码可以写成以下样式  直接返回结果
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# 一个函数建议最好是返回一种类型的数据
def get_month_day(year, month):
    """
        根据年月份判断天数
    :param year: 目标年份
    :param month: 目标月份
    :return: 天数结果  int
    """
    if month < 1 or month > 12:
        return 0
    if month == 2:
        # if is_leap_year(year):
        #     return 29
        # else:
        #     return 28
        # 以上代码 可以写成 if 的条件表达式
        return 29 if is_leap_year(year) else 28
    if month in (4,6,9,11):
        return 30
    return 31

print(get_month_day(2024, 2))