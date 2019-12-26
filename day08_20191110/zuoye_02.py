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
    list_result = []
    # 外层循环生成需要判断的整数
    for number in range(start_number, end_number):
        # 内层循环是判断是否是素数
        for item in range(2, number):
            if number % item == 0:
                break
        else:
            list_result.append(number)
    return list_result


# 调用函数
print(judge_range_prime_number(5, 120))
