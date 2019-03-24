import math

class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        return int(self.fibonacci(number+1))

    def fibonacci(self, n):
        xn = 1 / (5 ** 0.5) * (math.pow(((1 + (5 ** 0.5)) / 2), n) - math.pow(((1 - (5 ** 0.5)) / 2), n))
        return xn
