# -*- coding:utf-8 -*-
# 
"""
题目url: https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
描述：
   给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
   找到所有在 [1, n] 范围之间没有出现在数组中的数字。
   您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
"""


class Solution:
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 利用 1 ≤ nums[i] ≤ n, 并且题目也没说不能破坏原数组, 顺序取反nums[i]
        for n in nums:
            i = abs(n) - 1
            if nums[i] > 0:
                nums[i] *= -1

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
        
        
res = Solution().findDisappearedNumbers([3,2, 1,2])
print(res)

