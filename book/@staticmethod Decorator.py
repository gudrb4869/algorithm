class CLASS:
    def a(self):
        pass

    @staticmethod
    def b():
        pass

print(type(CLASS.a), type(CLASS.b))
cls = CLASS()
print(type(cls.a), type(cls.b))