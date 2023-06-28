class Singleton:
    __instance = None

    def __init__(self, name):
        if not Singleton.__instance:
            self.name = name

    @classmethod
    def getinstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton(cls)
        return cls.__instance


s = Singleton("ajay")
print("Object created", s.getinstance())
print(s.name)
s1 = Singleton
print("Object created", s.getinstance())
