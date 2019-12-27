"""
    正则表达式
"""
import re

# ['Hello', 'Word']
# a = re.findall('\S+', "Hello     Word")

# ['Hello', 'Word']
# a = re.findall('[A-Z][a-z]*', "Hello     Word")

# ['Hello     Word']
# a = re.findall('\w+\s+\w+', "Hello     Word")

# ['Hello', 'Word', 'I', 'Is', 'Tom']  匹配所有大写字母
a = re.findall('[A-Z][a-z]*', "Hello     Word  how are    you I am Is Tom  ")

# ['Hello', 'Word', 'how', 'are', 'you', 'I', 'am', 'Is', 'Tom'] 匹配非空字符
# b = re.findall('[^ ]+', "Hello     Word  how are    you I am Is Tom  ")
# ['Hello', 'Word', 'how', 'are', 'you', 'I', 'am', 'Is', 'Tom']
b = re.findall('\S+', "Hello     Word  how are    you I am Is Tom  ")

# print(a)
# print(b)

# 原生字符串
c = re.findall('\\\\', "\\")
print(c)    # ['\\']

s = "hello \n word"
s2 = r"hello \n word"
print(s)
print(s2)   # hello \n word