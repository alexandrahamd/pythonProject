class MyInt:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if self.__check(other):
            return self.x + int(other)

    def __sub__(self, other):
        if self.__check(other):
            return self.x - int(other)

    def __mul__(self, other):
        if self.__check(other):
            return self.x * int(other)

    def __truediv__(self, other):
        if self.__check(other):
            return self.x / int(other)

    @classmethod
    def __check(cls, x):
        if not isinstance(x, (int, str)):
            return False
        return True

    def __repr__(self):
        return f"{self.__class__}: {self.x}"

a = MyInt(5)
print(a)
a = a + 5
print(a)
a = a - 5
print(a)
a = a * 2
print(a)
a = a / 2
print(a)