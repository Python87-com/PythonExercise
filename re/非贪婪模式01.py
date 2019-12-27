"""
    贪婪模式
    匹配的条件后加 ? 就会变成非贪婪模式
"""
import re

a = re.findall('ab*?',"abbbbbbbbbbbcd")
print(a) # ['a']

a = re.findall('ab+?',"abbbbbbbbbbbcd")
print(a) # ['ab']

a = re.findall('ab??',"abbbbbbbbbbbcd")
print(a) # ['a']

a = re.findall('ab{3}?',"abbbbbbbbbbbcd")
print(a) # ['abbb']

a = re.findall('ab{3,5}?',"abbbbbbbbbbbcd")
print(a) # ['abbb']