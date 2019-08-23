# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        map = {}
        for value in array:
            if map.__contains__(value):
                del map[value]
            else:
                map[value] = 1
        return map.keys()

Solution().FindNumsAppearOnce([2,4,3,6,3,2,5,5])
