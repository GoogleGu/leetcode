"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6)
"""

class Louzy_Solution:

    cache = dict()
    def numDecodings(self, s: str) -> int:
        self.cache = dict()
        if not s:
            return 0
        return self._num_of_decodings(s)

    def _num_of_decodings(self, s):
        if len(s) <= 1:
            return self._isvalid(s)

        return self._split_and_count(s, 1) + self._split_and_count(s, 2)


    def _split_and_count(self, s, split_index):
        count = 0
        validity = self._isvalid(s[:split_index])
        if validity:
            cut_off = s[split_index:]
            if self.cache.get(cut_off) is None:
                self.cache[cut_off] = self._num_of_decodings(cut_off)
            count = self.cache[cut_off]
        return count

    def _isvalid(self, s):
        if s and (int(s) > 26 or s[0] == '0'):
            return 0
        else:
            return 1


class Solution:

    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [1 for _ in s]

        for i in range(1, len(s)):
            last_c, c = s[i-1], s[i]
            if c == '0' and (last_c != '1' and last_c != '2'):
                return 0
            elif last_c == '0':
                dp[i] = dp[i-1]
            elif c == '0':
                dp[i] = dp[i-2]
            elif last_c == '1' or (last_c == '2' and (int(c) <= 6)):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.numDecodings("230"))
