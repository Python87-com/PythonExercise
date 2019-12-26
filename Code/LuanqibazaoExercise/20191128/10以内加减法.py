import random

# for x in range(1, 6):
#     for y in range(1, 6):
#         print("{0} + {1} = (   )".format(x, y), end=" ")
#     print()
# x1 = random.randint(1, 10)
# x2 = random.randint(1, 10)
# print(s1)
# for x in range(1, 10):
#     for y in range(1, 10):
#         print("{0} + {1} = (   )".format(x1, x2), end=" ")
#     print()
count = 0
while count < 30:
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    print("{0} + {1} = (   )".format(x1, x2), end=" ")
    print()
    count += 1

# -
# for x in range(10):
#     for y in range(1,10):
#         if x > y:
#             print("{0} - {1} = (   )".format(x, y),end = " ")
#     print()
