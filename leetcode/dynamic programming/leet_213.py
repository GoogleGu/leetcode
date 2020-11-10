class Solution:
    cache = dict()

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.cache = dict()
        skip_first = self._sub_rob(nums[1:], 0)
        self.cache = dict()
        rob_last = self._sub_rob(nums[:-1], 0)
        return max(skip_first, rob_last)

    def _sub_rob(self, nums, start):
        if self.cache.get(start) is not None:
            return self.cache[start]
        
        if start >= len(nums):
            return 0

        result = max(self._sub_rob(nums, start+1), nums[start] + self._sub_rob(nums, start+2))
        self.cache[start] = result
        return result