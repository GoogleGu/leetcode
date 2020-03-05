# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        total = n and self.Sum_Solution(n-1)
        return n + total