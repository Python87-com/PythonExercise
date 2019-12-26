import copy
# a = (1)
#
# print(type(a))
#
# print(1 + 2 *2 **3 + 6//3)
#
# apple = mango
# print(apple)

# a = [1,2,3]
# print(a *3)

# print(24%5)
#
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x[0][1])

# class A(object):
#     pass
#
#
# class B(A):
#     pass
#
#
# b = B()
# print(issubclass(b, B) == True)

# class Test:
#        def prt(self):
#             print(self)
#             print(self.__class__)
#
#
# t = Test()
# t.prt()


# class A:
#         def __init__(self,args):
#             self.__p = args
#
#
#         def __priavte(self):
#             print('我是私有方法')
#
#         def showA(self):
#             print("self.__p=",self.__p)
#             self.__priavte()
#
# a = A(100)
# a.showA()


# class Shape():
#         def draw(self):
#             self.drawSelf()
#
# class Point(Shape):
#         def drawSelf(self):
#             print("正在画一个点")
#
#
# class Circle(Shape):
#         def drawSelf(self):
#             print("正在画一个圆")
#
# shape = Point()
# shape.draw()
#
# shape = Circle()
# shape.draw()

# a = [1,2,3,["a","b"]]
# b = copy.copy(a)
# a[3].append(5)
# print(b)

# class ParentClass1:
#     pass
#
# class ParentClass2:
#     pass
#
# class SubClass1(ParentClass1):
#     pass
#
# class SubClass2(ParentClass1,ParentClass2):
#     pass
#
# print(ParentClass1)
# print(ParentClass2)
# print(SubClass1)
# print(SubClass2)

class A:
        def hello(self):
            print('A类的hello')


class B(A):
        def hello(self):
            print('B类的hello')

b = B()
super(B,b).hello()