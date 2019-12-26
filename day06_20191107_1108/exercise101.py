"""
    练习：在控制台中录入多个人的多个喜好，输入空字符停止
    例如：
        请输入姓名：
        请输入第1个喜好：
        请输入第2个喜好：
        ...
        请输入姓名：
        ...
        最后在控制台上打印所有人的所有喜好   【字典嵌套字典做】
"""
# 多人信息 字典
dict_people_info = {}

while True:
    people_name = input("请输入姓名：")
    if people_name == "":
        break

    count = 0
    # 爱好 列表
    tuple_likes = ("like1", "like2", "like3")
    list_likes_info = {}
    while count < 3:
        like = input("请输入第{0}个喜好:".format(count + 1))
        if like == "":
            print("喜好不能为空,请重新输入")
            continue
        else:
            # 从元组中取 爱好
            list_likes_info[tuple_likes[count]] = like
            # 计数
            count += 1
    # 把喜好和名字对应到一起
    dict_people_info[people_name] = list_likes_info


print(dict_people_info)
# 打印  字典套列表
for name, values in dict_people_info.items():
    print("{0}的喜好分别是{1}、{2}、{3}。".format(name, values["like1"], values["like2"], values["like3"]))








