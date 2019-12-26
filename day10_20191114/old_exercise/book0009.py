import copy

# dict1 = {}
#
# dict2 = {3: 5}
#
# # dict3 = {[1, 2, 3]: "uestc"}
#
# dict4 = {(1, 2, 3): "uestc"}
#
# print(dict1)
# print(dict2)
# # print(dict3)
# print(dict4)

# list01 = list(map(lambda x:x + 1,[1,2,3]))
# print(list01)   # [2, 3, 4]


# a = 1
# b = 2*a/4
# a = "none"
# print(a,b)      # none 0.5

a = [1, 2, 3, 4, ['a', 'b']]

b = a

c = copy.copy(a)

d = copy.deepcopy(a)

a.append(5)
a[4].append('c')
print(c)
# print(a)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]

# s = set('python')[0]
# print(s)

# print(1.2 - 1.0 == 0.2)  # False
#
# e = 1.2 - 1.0
# e2 = 0.2
#
# print(e == e2)
#
# result = [i ** i for i in range(3)]
# for i in range(3):
#     print(i ** i)
#
# print(result)
#
# print(0 ** 0)
#
# tuple01 = (1, 2, 3)
# del tuple01
# print(tuple01)


def genfn():
    def print_hello():
        print('Hello word')
    return print_hello

fn = genfn()
fn()
print(fn())

# a = 'a'
# print(a > 'a' or 'c')   # c

b = 2 * a / 4
a = "one"
print(a,b)












