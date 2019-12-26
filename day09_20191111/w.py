count = 1
# 纸张厚度
thickness = 0.01
# while 循环里需要计算单位的一致性，如果改成米的话，则前面输出的厚度会出现科学计数法
while thickness < 8848430:
    thickness = thickness * 2  # 这里也可以写成 thickness *= 2 效果是一样的
    count += 1
    print(thickness)
print(count - 1)
