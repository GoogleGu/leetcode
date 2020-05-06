class Solution:
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
            print(num, tails)

        return max_len


if __name__ == '__main__':
    input = [1, 10,9,2,6, 5,3,4]
    sol = Solution()
    print(sol.lengthOfLIS(input))