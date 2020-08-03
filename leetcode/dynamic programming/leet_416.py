import pprint

class Solution:
    def canPartition(self, nums):

        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]

        for n_num in range(len(nums)):
            for n_sum in range(target+1):
                # 条件转移公式
                # 两种选择：将当前数字加到sum中或不加到sum中
                if n_sum == nums[n_num]:
                    dp[n_num][n_sum] = True
                elif n_sum - nums[n_num] > 0:
                    dp[n_num][n_sum] = dp[n_num-1][n_sum] or dp[n_num-1][n_sum-nums[n_num]]
                else:
                    dp[n_num][n_sum] = dp[n_num-1][n_sum]
        return dp[-1][-1]
    
if __name__ == "__main__":
    print(Solution().canPartition([1,2,3,6]))