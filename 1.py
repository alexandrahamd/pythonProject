import math

class Derivative:
    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        return (self.func(x + 0.0001) - self.func(x)) / 0.0001

# Считаем производную
@Derivative
def sin_(x):
    return math.sin(x)

print(sin_(math.pi/3))
#0.4999566978958203