"""
    在控制台中获取月份
    打印天数  输入有误
    1 3 5 7 8 10 12 ---> 31天
    4 6 9 11 ---> 30天
    2   ---> 28天

"""

def get_month_day(month):
    """
        根据月份判断天数
    :param month: 目标月份
    :return: 返回天数结果 str
    """
    if month < 1 or month > 12:
        return "输入有误。"
    if month == 2:
        return "28天"
    if month in (4,6,9,11):
        return "30天"
    else:
        return "31天"

print(get_month_day(5))
