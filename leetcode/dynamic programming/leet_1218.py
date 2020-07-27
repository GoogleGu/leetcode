class Solution:
    def longestSubsequence(self, arr, difference):
        """
        核心思想：
        dp[i]定义为之前的序列中，数字i对应的最长等差子序列的长度
        状态转移方程为
        dp[j] = max(1, dp[i - difference] + 1)
        因为j数字对应的最长等差子序列长度要么就是在之前的这个j-difference数字上加1，要么就是从头算起也就是1。
        """
        dp = dict()
        for num in arr:
            dp[num] = dp.get(num-difference, 0) + 1
        return max(dp.values())


if __name__ == "__main__":
    arr = [1,5,7,8,5,3,4,2,1]
    print(Solution().longestSubsequence(arr, -2))
