"""
5.(扩展)计算一个字符串中的字符以及出现的次数.
# 思想：
# 逐一判断字符出现的次数.
# 如果统计过则增加１，如果没统计过则等于１.

abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
"""
str_user = "asddkjskldjhgjkgjghjgjgjiuhuiygvjllll"

frequency = {}

for item in str_user:
    if item not in frequency:
        frequency[item] = 1
    else:
        frequency[item] += 1

for key, value in frequency.items():
    print("{0}出现{1}次".format(key, value))
