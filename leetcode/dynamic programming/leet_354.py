class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda i: (i[0], -i[1]))
        nums = [i[1] for i in envelopes]
        return self.lengthOfLIS(nums)

    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        tails = {1: nums[0]}
        max_len = 1
        # 对第二个数字进行处理
        for num in nums[1:]:
            # 从最长的序列开始看，是否可以拼接在后面，如果可以，就拼在后面记录下来，这个数字就处理完毕了
            for length in range(max_len, 0, -1):
                tail = tails[length]
                if num > tail:
                    tails[length+1] = num
                    if length == max_len:
                        max_len += 1
                    break
            else:
                # 如果这个数字完全拼不进去，说明是已记录的最小值，用它替换长度为1的序列
                tails[1] = num

        return max_len


    def raw_dp(self, envelopes):
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0], x[1]))

        dp = [1 for _ in range(len(envelopes))]
        for i in range(len(envelopes)):
            for j in range(i):
                small, big = envelopes[j], envelopes[i]
                if small[0] < big[0] and small[1] < big[1]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

if __name__ == '__main__':
    print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))