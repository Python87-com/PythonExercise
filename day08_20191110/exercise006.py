"""
练习：定义函数 根据年月，计算有多少天，考虑闰年
    在控制台中获取月份
    打印天数  输入有误
    1 3 5 7 8 10 12 ---> 31天
    4 6 9 11 ---> 30天
    2   ---> 28天    闰年 29天

"""

def get_month_day(year, month):
    """
        根据年月份判断天数
    :param year: 目标年份
    :param month: 目标月份
    :return: 返回天数结果 str
    """
    if month < 1 or month > 12:
        return "输入有误。"
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return "29天"
        else:
            return "28天"
    if month in (4,6,9,11):
        return "30天"
    return "31天"

print(get_month_day(2024, 2))
