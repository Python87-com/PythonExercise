"""
    练习 古代一斤等于16两
    写出函数 计算是多少斤多少两
"""
def ancientUnitConversion(number):
    """
        古代单位转换 根据两计算几斤几两
    :param number: 两 int
    :return: 转换后的结果（可以是列表，或 元组数据）
    """
    # 逻辑运算
    # 斤 取商//
    result_jin = number // 16
    # 两 取余 %
    result_liang = number % 16
    # return (result_jin, result_liang)
    return [result_jin, result_liang]


result = ancientUnitConversion(105)

# 这里就直接显示结果  不单独提取出来了
print(result)