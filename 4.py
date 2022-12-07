class MyInt:
    def __init__(self, x):
        self.x = x

    @classmethod
    def __check(cls, other):
        if not isinstance(other, (str, int, MyInt)):
            raise TypeError("Операнд справа должен иметь тип int или MyInt")

        return int(other) if isinstance(other, (str, int)) else other.x
    
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
a = a < 2
print(a)
a = a <= 2
print(a)
a = a > "5"
print(a)
