"""
    根据年月日（生日）,计算自己活了多少天
    思路：1970.1.1 到 生日那天的时间戳
    在获取到今天的时间戳
    今天的时间戳 - 生日那天的时间戳 = 等于 自己活了多少秒的时间戳
"""
import time


def get_day(year, month, day):
    """
        根据出生年月日获取活了多少天
    :param year:年
    :param month:月
    :param day:日
    :return:int 活了多少天
    """
    # 把 生日年月日转换成 时间元组
    birthday_time_tuples = time.strptime("{0}-{1}-{2}".format(year, month, day), "%Y-%m-%d")
    # 生日时间元组转换成时间戳
    s_time = time.mktime(birthday_time_tuples)
    # 获取当前时间的时间戳
    local_time_tuples = time.time()

    result = local_time_tuples - s_time

    # 返回一个整数
    return int(result // (24 * 60 * 60))


re = get_day(1987, 10, 24)
print("活了{}天".format(re))
# 11721.0
# 11721.845732696227
