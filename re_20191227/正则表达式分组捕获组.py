"""
正则表达式分组（子组） 中的 捕获组
可以给正则表达式子组起一个名字，表达该子组的意义，这种有名字的子组就称之为 捕获组
格式 (?P<name>)
"""
import re

s = re.search(r'(?P<pig>ab+)',"ababababab").group('pig')

print(s)    # ab

# 一个正则表达式中可以包含多个子组
# s2 = re.search(r'((ab)c)d(?P<pig>ef)',"abcde1fdefjjssabsdlkf").group()
# print(s2) # 报错：AttributeError: 'NoneType' object has no attribute 'group'

s3 = re.search(r'((ab)c)d(?P<pig>ef)',"abcdef1fdefjjssabsdlkf").group()
print(s3)   # abcdef



