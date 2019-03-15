import math


class Solution:
    def Fibonacci(self, n):
        xn = 1 / (5 ** 0.5) * (math.pow(((1 + (5 ** 0.5)) / 2), n) - math.pow(((1 - (5 ** 0.5)) / 2), n))
        return xn

    def jumpFloor(self, n):
        # 斐波那契数列（从2开始）
        n += 1
        return self.Fibonacci(n)

    def jumpFloorII(self, number):
        # 斐波那契数列的阶加 => fn = 2* f(n-1)
        # f1 = 1
        # f2 = f1 + 1 = 2
        # f3 = f1 + f2 + 1 = 4
        # f4 = f3 + f2 + f1 + 1 = 8
        if number == 1:
            return 1
        result = 0
        for i in range(0, number-2):
            result += self.jumpFloorII(i+1)
        return 2*(result+1)
