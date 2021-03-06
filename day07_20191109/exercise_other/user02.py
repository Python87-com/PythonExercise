"""
使用一个字典来存储一些人喜欢的数字。请想出5 个人的名字，
并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储
在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保
数据是真实的
"""
"""
    '张三'： [5, 7, 8, 1, 0]
    '李四'： [1, 5, 9, 7, 4]
    '王五'： [5, 8, 9, 3, 0]
    '赵钱'： [1, 3, 5, 8, 9]
    '悟空'： [1, 3, 6, 7, 8]
"""
user = {
    '张三': [5, 7, 8, 1, 0],
    '李四': [1, 5, 9, 7, 4],
    '王五': [5, 8, 9, 3, 0],
    '赵钱': [1, 3, 5, 8, 9],
    '悟空': [1, 3, 6, 7, 8]
}

for item, values in user.items():
    for num in values:
        print("{}喜欢的数字是：{}".format(item, num))

"""
张三喜欢的数字是：5
张三喜欢的数字是：7
张三喜欢的数字是：8
张三喜欢的数字是：1
张三喜欢的数字是：0
李四喜欢的数字是：1
李四喜欢的数字是：5
李四喜欢的数字是：9
李四喜欢的数字是：7
李四喜欢的数字是：4
王五喜欢的数字是：5
王五喜欢的数字是：8
王五喜欢的数字是：9
王五喜欢的数字是：3
王五喜欢的数字是：0
赵钱喜欢的数字是：1
赵钱喜欢的数字是：3
赵钱喜欢的数字是：5
赵钱喜欢的数字是：8
赵钱喜欢的数字是：9
悟空喜欢的数字是：1
悟空喜欢的数字是：3
悟空喜欢的数字是：6
悟空喜欢的数字是：7
悟空喜欢的数字是：8
"""
