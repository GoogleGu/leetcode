# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        position = 1
        result = 0
        for char_index in range(len(s)-1, -1, -1):
            char = s[char_index]
            ascll = ord(char)
            if ascll < 48 or ascll > 57:
                if char_index == 0 and char == '+':
                    return result
                if char_index == 0 and char == '-':
                    return result * -1
                else:
                    return 0
            result += position * (ascll - ord("0"))
            position = 10 * position
        return result


print(Solution().StrToInt("-123"))
