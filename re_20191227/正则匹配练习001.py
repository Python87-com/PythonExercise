"""
正则匹配练习01

1、匹配一个.com邮箱格式字符串
2、匹配一个密码 8-12位数字字母下划线构成
3、匹配一个数字  正数，负数，整数，小数，分数1/2，百分数45%
4、匹配一段文字，中以大写字母开头的单词，注意文中可能有iPython(不算)，H-base(算)
单词可能有大写字母 小写字母 下划线

"""
import re
# 1、匹配一个.com邮箱格式字符串
a = re.findall('\w+@\w+\.com',"10293665@qq.com,316966595@qq.com,ssk@163.com,lvze@163.com")
print(a)
# ['10293665@qq.com', '316966595@qq.com', 'ssk@163.com', 'lvze@163.com']

# 2、匹配一个密码 8-12位数字字母下划线构成
mima = re.findall('\w{8,12}',"520_kj45,S52e_8p4,Ss0F52o8,sSdrtsdt,__dss854")
print(mima)
# ['520_kj45', 'S52e_8p4', 'Ss0F52o8', 'sSdrtsdt', '__dss854']

# 3、匹配一个数字  正数，负数，整数，小数，分数1/2，百分数45%
sz = re.findall('-?\w+\.?\/?%?\w*',"10,-36,-3.66,0.55,5/6,95%,-52,658")
print(sz)
# ['10', '-36', '-3.66', '0.55', '5/6', '95%', '-52', '658']
sz2 = re.findall('-?\d+\.?\/?%?\d*',"10,-36,-3.66,0.55,5/6,95%,-52,658")
print(sz2)
# ['10', '-36', '-3.66', '0.55', '5/6', '95%', '-52', '658']

# 4、匹配一段文字，中以大写字母开头的单词，注意文中可能有iPython(不算)，H-base(算)
# 单词可能有大写字母 小写字母 - 下划线
words = "Hooray! It's snowing! It's time iPython to_2 make H-base a snowman.James runs out. He makes a big pile of snow. He puts a big snowball on top. He adds a scarf and a hat. He adds an orange for the nose. He adds coal for the eyes and buttons.In the evening, James opens the door. What does he see? The snowman is moving! James invites him in. The snowman has never been inside a house. He says hello to the cat. He plays with paper towels.A moment later, the snowman takes James's hand and goes out.They go up, up, up into the air! They are flying! What a wonderful night!The next morning, James jumps out of bed. He runs to the door.He wants to thank the snowman. But he's gone."
word = re.findall(r'\b[A-Z]\'?\-?\_?\w*',words)
print(word)
"""
\b[A-Z]\'?\-?\w*
\b 匹配边界
[A-Z]匹配大写字母
\'?  匹配 ' 符号  没有成功？？？
\-?  匹配 - 符号
\w* 匹配 - 后面所有的字符
"""
# It's  中的  ' 没有匹配出来   \'?  这个匹配不出来？？？
# ['Hooray', 'It', 'It', 'H-base', 'James', 'He', 'He',.......]

word2 = re.findall(r'\b[A-Z][\'-_a-zA-Z]*',words)
print(word2)
# ['Hooray', "It's", "It's", 'H-base', 'James', 'He'.....]