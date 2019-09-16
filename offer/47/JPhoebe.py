# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        sum = n and self.Sum_Solution(n - 1)
        return n + sum


print(Solution().Sum_Solution(3))
