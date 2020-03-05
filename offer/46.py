# -*- coding:utf-8 -*-
class Solution:

    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1

        res = 0
        for i in range(0, n-1):
            res = (res + m) % (n-i)
        return res
