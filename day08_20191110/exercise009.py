"""
    定义列表升序排列的函数
"""
def list_sort(sort_list):
    # 满足以下2个条件，就无需通过返回值传递结果。
    # 1、传入的是可变对象
    # 2、函数体修改的是传入的对象
    for x in range(len(sort_list) - 1):
        for y in range(x + 1, len(sort_list)):
            if sort_list[x] > sort_list[y]:
                sort_list[x], sort_list[y] = sort_list[y], sort_list[x]
    # return sort_list

list01 = [11, 5, 71, 19, 12]
# 调用函数
list_sort(list01)
print(list01)