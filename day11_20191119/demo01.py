"""
[
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"]
]
在二维列表中，获取13位置，向左，3个元素
在二维列表中，获取22位置，向上，2个元素
在二维列表中，获取03位置，向下，2个元素
"""
# print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
#
# print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))
#
# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#
# print('\n'.join([''.join(['*' if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0 else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else ' ' for x in range(-80,20)]) for y in range(-20,20)]))
#

dict01 = {1: 0, 2: 3}

print(len(dict01))