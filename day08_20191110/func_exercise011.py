"""
    练习：定义函数，根据小时、分钟、秒。计算总秒数
    要求： 可以只计算小时---.>秒
        可以只计算分钟---.>秒
        可以只计算小时+分钟--->秒
        可以只计算分钟+秒 --->秒
"""
def hour_minute_second_add(h=0,m=0,s=0):
    return (h * 60 * 60) + (m * 60) + s


# 调用函数
print(hour_minute_second_add(1,2,3))        # 3723
print(hour_minute_second_add(h=1,m=36))     # 5760
print(hour_minute_second_add(m=10,s=36))    # 636
print(hour_minute_second_add(h=1))          # 3600
print(hour_minute_second_add(m=10))         # 600


