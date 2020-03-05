# -*- coding:utf-8 -*-
class Solution:

    numbers = {str(num): num for num in range(10)}

    def StrToInt(self, s):

        total = 0
        sign = 1
        sign_appeared = False
        for char in s:
            if sign_appeared:
                if char in ['+', '-']:
                    return 0
            if char == '+':
                sign_appeared = True
                continue
            elif char == '-':
                sign_appeared = False
                sign = -1
                continue
            elif self.numbers.get(char) is None:
                return 0
            total *= 10
            total += self.numbers[char]
        return total * sign


