# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        
        if number <= 3:
            return number - 1

        mult = 1
        while number > 3:
            if number % 2 == 0:
                number -= 2
                mult *= 2
            else:
                number -= 3
                mult *= 3
        return mult * number
