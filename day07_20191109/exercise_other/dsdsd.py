# 获取第一个数
num01 = float(input("请输入第一个数："))
# 获取第二个数
num02 = float(input("请输入第二个数："))
# 获取的运算符为字符串
operator = input("请输入一个运算符(如：+ , - , * , /)：")
# 逻辑运算
if operator == "+":
    print("{0} {1} {2} = {3}".format(num01, operator, num02, (num01 + num02)))
elif operator == "-":
    print("{0} {1} {2} = {3}".format(num01, operator, num02, (num01 - num02)))
elif operator == "*":
    print("{0} {1} {2} = {3}".format(num01, operator, num02, (num01 * num02)))
elif operator == "/":
    print("{0} {1} {2} = {3}".format(num01, operator, num02, (num01 / num02)))
else:
    print("请输入正确的运算符(如：+ , - , * , /)!!!")
