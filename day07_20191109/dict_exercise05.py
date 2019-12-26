"""
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
"""
for x in range(4):
    for y in range(6):
        if y % 2 == 1:
            print("#", end=" ")
        else:
            print("*",end = " ")
    print()