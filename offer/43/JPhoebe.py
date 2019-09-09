# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        return s[n:]+s[:n]


print(Solution().LeftRotateString("abcXYZdef", 3))
