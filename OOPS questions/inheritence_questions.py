'''Question 1'''

# class Test:
#     def __new__(self):
#         self.__init__(self)
#         print("Test __new__() invoked")
#     def __init__(self):
#         print("Test __init__() invoked")
# class Derived_Demo(Test):
#     def __new__(self):
#         print("Derived_Test __new__() invoked")
#     def __init__(self):
#         print("Derived_Test __init__() invoked")
#
#
# obj1 = Derived_Demo()
# # obj2 = Demo()


'''Question 2'''

# class A:
#     def one(self):
#         return self.two()
#
#     def two(self):
#         return 'A'
#
#
# class B(A):
#     def two(self):
#         return 'B'
#
#
# obj1 = A()
# obj2 = B()
# print(obj1.one(), obj2.two())


'''Question 3'''
#
# class A:
#     def __init__(self):
#         self.__i = 1
#         self.j = 5
#
#     def display(self):
#         print(self.__i, self.j)
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.j= 4
#
# c = B()
# c.display()


'''Question 4'''

# class Test:
#     def __init__(self):
#         self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#         super().__init__()
#         self.y = 1
# b = Derived_Test()
# print(b.x,b.y)


'''Question 5'''

# class A:
#     def __init__(self,x):
#         self.x = x
#     def count(self,x):
#         self.x = self.x+1
# class B(A):
#     def __init__(self, y=0):
#         A.__init__(self, 3)
#         self.y = y
#     def count(self):
#         self.y += 1
#
# obj = B()
# obj.count()
# print(obj.x, obj.y)


'''Question 6'''

# class A:
#     def __init__(self):
#         self.__x = 1
# class B(A):
#     def display(self):
#         super().__init__()
#         print(self.__x)
#
# obj = B()
# obj.display()


'''Question 7 '''

# class A:
#     def __init__(self):
#         self._x = 5
# class B(A):
#     def display(self):
#         print(self._x)
# obj = B()
# obj.display()


'''Question 8'''


class A:
    """
    Class C defines a test() method, so that method is called. The test() method of class C prints "test of C called"
    and then calls super().test(), which invokes the test() method of the next class in the MRO, which is class Z.
    """

    def test(self):
        print("test of A called")


class Z(A):
    def test(self):
        print('test of Z is called')
        super().test()


class B(A):
    def test(self):
        print("test of B called")


class C(A):
    def test(self):
        print("test of C called")
        super().test()


class D(C, Z, B):
    def test2(self):
        print("test of D called")


obj = D()
obj.test()
