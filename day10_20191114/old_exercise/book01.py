"""
    求 200以内 能被17整除的最大正整数
"""
# 以下循环得出的结果是 所有能被17整除的正整数
# for i in range(1, 200):
#     if i % 17 == 0:
#         print(i)

for i in range(200, 0, -1):
    if i % 17 == 0:
        print(i)    # 187
        break
