class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n > 0:
            n = n & (n-1)
            ones += 1
        return ones
