# -*- coding:utf-8 -*-
# 
"""
题目url: https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
描述：
    给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
    找到所有出现两次的元素。
    你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
"""


class Solution:
    
    # 同448 https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] > 0:
                nums[i] *= -1
            else:
                res.append(abs(n))
        return res
    
        
res = Solution().findDisappearedNumbers([3,2,1,2])
print(res)

