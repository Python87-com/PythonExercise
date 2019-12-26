"""
    练习：记录一个函数 fun01的执行次数
    画出内存图
"""
# 定义一个全局变量
count = 0

def fun01():
    print("我被执行了。")
    # 定义一个全局变量
    global count
    count += 1

# 调用函数
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()

print(count)

