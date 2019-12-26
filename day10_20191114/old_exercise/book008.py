"""
    创建一个列表用于存储用户输入的人物
"""

# 创建一个空列表
character = []

while True:
    str_name = input("请输入在西游记中您喜欢的人物名称：")
    # 输入空字符则退出并打印
    if str_name == "":
        for i in character:
            print(i)
        break
    else:
        character.append(str_name)
