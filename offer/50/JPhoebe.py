# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        result = []
        for num in numbers:
            if result.__contains__(num):
                duplication[0] = num
                return True
            result.append(num)
        return False

Solution().duplicate([2,1,3,0,4], [])
