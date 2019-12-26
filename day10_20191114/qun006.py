import random  # 导入随机数

list_number_random = []  # 存放红色球与蓝色球

for item in range(6):  # 重复六次
    random_number_red = random.randint(1, 34)
    # 随机生成1-33之间的红色球
    if random_number_red not in list_number_random:
        list_number_random.append(random_number_red)
        # 如果红色球不在列表中，加进去
    else:
        print("号码已经重复")  # 如果已经在了，则提醒重复了
        continue
for item in range(1):  # 重复1次
    # 随机生成1-16的蓝色球
    random_number_blue = random.randint(1, 17)
    # 把蓝色的球加红色球的列表中
    list_number_random.append(random_number_blue)

# result = "".join(list_number_random)
# print(result)

print(list_number_random)

# 手动输入彩票
# list_number = []
# while len(list_number) < 6:
#     number = int(input("请输入第%d红色的球" % (len(list_number) + 1)))
#     if number < 1 or number > 33:
#         print("输入有误，请重新输入")
#         continue
#     if number not in list_number:
#         list_number.append(number)
#     else:
#         print("输入重复，请重新输入！")
# print(list_number)
# while True:
#     # 当长度为6时，则意味着红色球输入完毕，蓝色球开始录入
#     blue_ball = int(input("请输入蓝色球："))
#     if blue_ball > 16 or blue_ball <= 0:
#         print("输入有误，请重新输入！范围应该是1-16")
#         continue
#     else:
#         list_number.append(blue_ball)
#         break
