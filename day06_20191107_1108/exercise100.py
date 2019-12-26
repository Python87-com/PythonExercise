"""
    练习：在控制台中录入多个人的多个喜好，输入空字符停止
    例如：
        请输入姓名：
        请输入第1个喜好：
        请输入第2个喜好：
        ...
        请输入姓名：
        ...
        最后在控制台上打印所有人的所有喜好   【字典嵌套列表做】
"""
# 多人信息 字典
dict_people_info = {}

while True:
    people_name = input("请输入姓名：")
    if people_name == "":
        break
    # dict_people_info["name"] = people_name
    count = 1
    # 爱好 列表
    list_likes_info = []
    while count < 4:
        like = input("请输入第{0}个喜好:".format(count))
        if like == "":
            print("喜好不能为空,请重新输入")
            continue
        else:
            list_likes_info.append(like)
            # 将 喜好合并到字典中
            count += 1

    dict_people_info[people_name] = list_likes_info


print(dict_people_info)
# 打印  字典套列表
for name, values in dict_people_info.items():
    print("{0}的喜好分别是{1}、{2}、{3}。".format(name, values[0], values[1], values[2]))








