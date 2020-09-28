"""
在计算机界中，我们总是追求用有限的资源获取最大的收益。

现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。

你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

 

示例 1:

输入: strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出: 4
解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
示例 2:

输入: strs = ["10", "0", "1"], m = 1, n = 1
输出: 2
解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。

"""
import pprint

class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for seq in strs:
            cost_1 = seq.count('1')
            cost_0 = seq.count('0')
            for v_0 in range(m, cost_0-1, -1):
                for v_1 in range(n, cost_1-1, -1):
                    dp[v_0][v_1] = max(dp[v_0][v_1], 1 + dp[v_0-cost_0][v_1-cost_1])
        return dp[-1][-1]
        
if __name__ == "__main__":
    print(Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3))