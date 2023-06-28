class A:
    def __init__(self):
        self.name = "ajay"


a = A()
print("Object created at", a)
b = A()
print("Object created at", b)

print(a.__dict__)
print(b.__dict__)
