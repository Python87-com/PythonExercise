"""
    练习2：定义生成器函数 my_zip ,实现下列现象
        将多个列表的每个元素合成一个元组
"""
list02 = ["孙悟空", "猪八戒", "唐僧", "沙僧"]
list03 = [101, 102, 103, 104,105]

def my_zip(*args):
    for index in range(len(args)):
        yield index, args[index]

for item in my_zip(list02):
    print(item)