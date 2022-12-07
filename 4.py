class MyInt:
    def __init__(self, x):
        self.x = x

    @classmethod
    def __check(cls, x):
        if not isinstance(x, (int, str)):
            return False
        return True

    def __repr__(self):
        return f"{self.__class__}: {self.x}"

    def __gt__(self, other):
        if self.__check(other):
            return self.x > other

    def __lt__(self, other):
        if self.__check(other):
            return self.x < other

    def __ge__(self, other):
        if self.__check(other):
            return self.x >= other

    def __le__(self, other):
        if self.__check(other):
            return self.x <= other

a = MyInt(5)
print(a)
a = a > 5
print(a)
a = a <= 5
print(a)
a = a < 2
print(a)
a = a <= 2
print(a)