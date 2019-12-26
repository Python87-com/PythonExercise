"""

"""


def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


fun01(1, 2, 3, 4, c=1)

year = 0

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(29)
else:
    print(28)