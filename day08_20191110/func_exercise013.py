"""
    关键字形参
"""


# def fun04(a,*args):
#     print(a)
#     print(args)
# fun04(1)
# fun04(1,2,3,4)

def fun04(a, *args, b):
    print(a)
    print(args)
    print(b)

fun04(1, 2, 3, 4, 5, 6, 7, b=10)
