# Only one instance of the class is created.

class Singleton:
    def __new__(cls, *args, **kwargs):  # __new__ method is called before __init__ method.
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
