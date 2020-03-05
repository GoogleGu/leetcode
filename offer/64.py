# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        
        if size == 0:
            return []
        maxes = []
        for i in range(len(num) - size + 1):
            print(num[i:i+size-1])
            maxes.append(max(num[i:i+size]))
        return maxes


if __name__ == "__main__":
    results = Solution().maxInWindows([2,3,4,2,6,2,5,1],3)
    