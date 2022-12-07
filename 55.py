class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        self.seconds = seconds

    def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Правый операнд должен быть типом int")

        return self.seconds + other

c1 = Clock(1000)
c1 = c1 + 100
print(c1)