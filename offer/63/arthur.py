# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.stream = []

    def Insert(self, num):
        # 二分插入
        return

    def GetMedian(self):
        n = len(self.stream)
        if n % 2 == 0:
            return (self.stream[n//2] + self.stream[n//2 - 1]) / 2
        else:
            return self.stream[n//2]


class AVLSolution:

    def __init__(self):
        self.AVLtree = None
    
    def Insert(self, num):

        return