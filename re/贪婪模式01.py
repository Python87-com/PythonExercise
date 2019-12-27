"""
    贪婪模式
    匹配的都会选择至少1次，不会选择0次
"""
import re

a = re.findall('ab*',"abbbbbbbbbbbcd")
print(a) # ['abbbbbbbbbbb']

a = re.findall('ab+',"abbbbbbbbbbbcd")
print(a) # ['abbbbbbbbbbb']

a = re.findall('ab?',"abbbbbbbbbbbcd")
print(a) # ['ab']

a = re.findall('ab{3}',"abbbbbbbbbbbcd")
print(a) # ['abbb']

a = re.findall('ab{3,5}',"abbbbbbbbbbbcd")
print(a) # ['abbbbb']