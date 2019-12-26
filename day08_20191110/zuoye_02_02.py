"""
    定义函数，计算指定范围内的素数
    判断素数的练习在 day03-day04 的 37题
"""
"""
    素数：只能被1和自身整除的整数
    思路：排除法，使用2-当前数字之间的整数判断，如果存在被整除则不是素数
    2 3 5 7 11 13 17 19 23
"""


# 定义一个判断一定范围内的数是否是素数的函数
def judge_range_prime_number(start_number, end_number):
    """
        获取范围内的素数
    :param start_number: 开始值(包含)
    :param end_number: 结束值(不包含)
    :return: 返回指定范围内所有素数的列表
    """
    list_result = []
    # 外层循环生成需要判断的整数
    # for number in range(start_number, end_number):
    #     if is_prime(number):
    #         list_result.append(number)
    # return list_result
    # 可以简化为推导式
    return [number for number in range(start_number, end_number) if is_prime(number)]

def is_prime(number):
    """
        判断指定的整数是否为素数
    :param number: 指定的整数
    :return: True 是素数， False 不是素数
    """
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


# 调用函数
print(judge_range_prime_number(5, 30))
