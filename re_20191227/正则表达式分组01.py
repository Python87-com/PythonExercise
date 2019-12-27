"""
正则表达式 分组-子组
"""
import re

a = re.findall(r'ab+',"ababababab")
print(a)
# ['ab', 'ab', 'ab', 'ab', 'ab']

b = re.search(r'ab+',"ababababab").group()
print(b)
# ab

c = re.search(r'(ab)+',"ababababab").group()
print(c)
# ababababab

d = re.search(r'王|李\w{1,3}',"李时珍,李自成").group()
print(d)    # 李时珍

e = re.search(r'王|李\w{1,3}',"王者荣耀,王二麻子").group()
print(e)    # 王

f = re.search(r'(王|李)\w{1,3}',"李时珍,李自成").group()
print(f)    # 李时珍

g = re.search(r'(王|李)\w{1,3}',"王者荣耀,王二麻子").group()
print(g)    # 王者荣耀


