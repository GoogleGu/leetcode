class Solution:
    def maxProduct(self, nums):
        global_max = -100000
        min_v = max_v = 1

        for num in nums:
            if num < 0:
                min_v, max_v = max_v, min_v
            min_v = min(min_v * num, num)
            max_v = max(max_v * num, num)
            global_max = max(global_max, max_v)

        return global_max
