"""
最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

链接：https://leetcode-cn.com/problems/maximum-subarray
"""

class Solution:
    def maxSubArray(self, nums):
        max = nums[0]
        sum = 0
        for num in nums:
            if sum + num >= 0:
                sum += num
                if sum > max:
                    max = sum
            else:
                if num > max:
                    max = num
                sum = 0

        return max