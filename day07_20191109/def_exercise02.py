"""
练习：将下列循环封装到一个函数中，调用一次
for x in range(4):
    for y in range(x+1):
        print("*", end=" ")
    print()
"""
# 创建一个绘画的函数
def draw(a):
    for x in range(a):
        for y in range(x + 1):
            print("*", end = " ")
        print()

# 调用函数
draw(4)

draw(5)