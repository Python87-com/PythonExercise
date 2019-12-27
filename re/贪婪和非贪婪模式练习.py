"""
贪婪模式和非贪婪模式练习
"""
import re
s = re.findall(r'\[\w+\]',"[陆贞传奇],[新还珠格格],[楚乔传],[乘风破浪],[花千骨]")
print(s)
# ['[陆贞传奇]', '[新还珠格格]', '[楚乔传]', '[乘风破浪]', '[花千骨]']

# 贪婪模式
s1 = re.findall(r'\[.+\]',"[陆贞传奇],[新还珠格格],[楚乔传],[乘风破浪],[花千骨]")
print(s1)
# ['[陆贞传奇],[新还珠格格],[楚乔传],[乘风破浪],[花千骨]']

# 非贪婪模式
s1 = re.findall(r'\[.+?\]',"[陆贞传奇],[新还珠格格],[楚乔传],[乘风破浪],[花千骨]")
print(s1)
# ['[陆贞传奇]', '[新还珠格格]', '[楚乔传]', '[乘风破浪]', '[花千骨]']

print("-" * 50)
# 贪婪模式
# 匹配()及里面的内容
q1 = re.findall(r'\(.+\)',"a(bcdef)jhigklmno(pqrst)uvwxyz")
print(q1)
# ['(bcdef)jhigklmno(pqrst)']

# 非贪婪模式
q2 = re.findall(r'\(.+?\)',"a(bcdef)jhigklmno(pqrst)uvwxyz")
print(q2)
# ['(bcdef)', '(pqrst)']

