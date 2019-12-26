def fun02(a):
    a[0] = 100

list01 = [1]

fun02(list01)

print(list01[0])


def fun04(a):
    a[1] = [200]

list02 = [1, [2, 3]]

fun04(list02)

print(list02[1])    # [200]
print(list02)       # [1, [200]]