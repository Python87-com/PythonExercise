"""
    存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：region
        景区Scenic ：故宫,天安门,天坛.
        美食food: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头.
"""

# 菜单
dict_region_scenic_food = {
    "北京": {
        "景区": ["故宫", "天安门", "天坛"],
        "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山", "春熙路"],
        "美食": ["火锅", "串串香", "兔头"]
    }
}

# 调用北京所有的美食
print(dict_region_scenic_food["北京"]["美食"])

# 获取所有城市 相当于调用字典中的 key
for key in dict_region_scenic_food:
    print(key)

# 获取所有城市的景区
for k, v in dict_region_scenic_food.items():
    print(k,v["景区"])

