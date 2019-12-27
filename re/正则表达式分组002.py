"""
正则表达式 分组-子组02
获取文本元素
"""
import re

s = re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group()
print(s)    # https://www.baidu.com

s2 = re.search(r'(https|http|ftp|file)://\S+',"http://www.baidu.com").group()
print(s2)    # http://www.baidu.com

# 可以通过编程语言某些接口获取匹配内容中，子组对应内容中的部分。
s3 = re.search(r'(https|http|ftp|file)://\S+',"http://www.baidu.com").group(1)
print(s3)    # http

