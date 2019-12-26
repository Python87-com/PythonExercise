
"""
    九九乘法表
"""
for x in range(1, 10):
    for y in range(1, 10):
        if x >= y:
            print("{0} * {1} = {2}".format(x,y,x*y),end = " ")
    print()

