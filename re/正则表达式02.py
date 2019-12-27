"""
正则表达式 功能函数演示
"""
import re

# 目标字符串
s = "Alex:1994,Tom:2000"

# 正则表达式
partter = '\w+:\w+'

# re模块直接调用
rw = re.findall(partter,s)
print(rw)   # ['Alex:1994', 'Tom:2000']

# regex 对象 调用 compile
regex = re.compile(partter)
list1 = regex.findall(s)
print(list1)    # ['Alex:1994', 'Tom:2000']

partter2 = '(\w+):(\w+)'
regex2 = re.compile(partter2)
list2 = regex2.findall(s,0,12)
print(list2)    # [('Alex', '1994')]
list3 = regex2.findall(s)
print(list3)    # [('Alex', '1994'), ('Tom', '2000')]