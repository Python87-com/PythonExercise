"""
双色球 p120
随机生成
"""
import random
red = random.sample(range(1, 34), 6)
blue = random.sample(range(1, 17), 1)

print(red + blue)









# def doubleColor():
#     red = random.sample(range(1, 34), 6)
#     # blue = random.choice(range(1, 17))
#     blue = random.sample(range(1, 17), 1)
#     # return str(red) + '-' + str(blue)
#
#     return red + blue
#
#
# print(doubleColor())
