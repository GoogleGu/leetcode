from collections import Counter


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):

        inputs = Counter(nums)
        print(inputs)


