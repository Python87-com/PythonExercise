"""
    求 小于 100的最大素数
"""
for n in range(100, 1, -1):
    for i in range(2, n):
        if n % i == 0:
            break
        else:
            print(n)
            break
