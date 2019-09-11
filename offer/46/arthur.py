# -*- coding:utf-8 -*-
class Solution:

    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1

        boys = list(range(0, n))
        start = 0

        while len(boys) > 1:
            deleted = (start + m) % len(boys) - 1
            boys.pop(deleted)
            start = deleted if deleted >= 0 else 0

        return boys[0]
