from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0

        totals = [defaultdict(lambda :0) for _ in range(len(nums))]
        print(totals)
        totals[0][nums[0]] += 1
        totals[0][-nums[0]] += 1

        for i in range(1, len(nums)):
            num = nums[i]
            for total, freq in totals[i-1].items():
                totals[i][total+num] += freq
                totals[i][total-num] += freq

        print(totals)
        return totals[-1].get(S, 0)

if __name__ == '__main__':
    print(Solution().findTargetSumWays([1,1,1,1,1], 3))