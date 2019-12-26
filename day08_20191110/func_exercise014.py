"""
# 作业:调用fun07。
def fun07(a, b, *args, c, d, **kwargs):
    pass
"""


def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun07(1, 2, 3, 4, 5, 6, c=11, d=12, e=22, g=32)
"""
# fun07函数执行结果
1
2
(3, 4, 5, 6)
11
22
{'e': 22, 'g': 32}
"""