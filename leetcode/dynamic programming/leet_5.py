"""
最长回文子串
https://leetcode-cn.com/problems/longest-palindromic-substring

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        """
        解题思路：
        算法基于一个观察结果：
        所有的长度超过1的回文字符串都是由比它小的回文字符串两端添加字符得来的，比如ababa是由bab在两端添加a得来的。最小的回文字符串是单个
        字母组成的回文字符串。
        其中又分两种，
            - 长度为2的回文字符串是由长度为1的回文字符串添加一个与原来的字母相同的字母构建而来。
            - 长度超过2的回文字符串都是由比它长度小2的回文字符串在两端各添加一个相同字母构建而来。
        因此，使用动态规划制表，以长度为1和2的回文字符串为起点做表，依次算出长度更长的回文字符串，做表结束后查表即可。

        效率：
        执行用时 : 3824 ms , 在所有 Python3 提交中击败了 36.71% 的用户
        内存消耗 : 102.6 MB , 在所有 Python3 提交中击败了 5.01% 的用户
        """
        # 处理长度小于2的特殊输入
        if not s:
            return ''
        if len(s) == 1:
            return s[0]

        # 初始化一个n行的回文表，并填充上第一行和第二行
        max_index = len(s)-1
        palindromes = [[] for _ in range(len(s))]
        palindromes[0] = [(i, i) for i in range(len(s))]
        for start, end in palindromes[0]:
            if start-1>= 0 and s[start-1] == s[end]:
                palindromes[1].append((start-1, end))
            if end+1 <= max_index and s[start] == s[end+1]:
                palindromes[1].append((start, end+1))

        # 从第一行开始，逐行处理在该行回文的基础上生成的新回文。
        for r in range(len(s)):
            for start, end in palindromes[r]:
                if start-1 >= 0 and end+1 < max_index and s[start-1] == s[end+1]:
                    palindromes[r+2].append((start-1, end+1))

        # 从下向上查表，取出最长的回文
        for p in palindromes[::-1]:
            if p:
                start, end = p[0]
                return s[start: end+1]

    def longestPalindromeImproved(self, s: str) -> str:
        """
        解题思路：
        与之前一样，但是只保留三行，而不再存储整个表

        效率：
        执行用时 : 2780 ms , 在所有 Python3 提交中击败了 48.14% 的用户
        内存消耗 : 13.9 MB , 在所有 Python3 提交中击败了 34.52% 的用户
        """
        # 处理长度小于2的特殊输入
        if not s:
            return ''
        if len(s) == 1:
            return s[0]

        # 初始化前两行回文表
        max_index = len(s)-1
        current_palindromes = [(i, i) for i in range(len(s))]
        next_palindromes = []
        for start, end in current_palindromes:
            if start-1>= 0 and s[start-1] == s[end]:
                next_palindromes.append((start-1, end))
            if end+1 <= max_index and s[start] == s[end+1]:
                next_palindromes.append((start, end+1))

        new_palindromes = []
        longest_palindromes = None
        # 从current palindromes生成新的回文，存储在new_palindromes
        # 每次迭代向前递进一个回文字符串长度
        while current_palindromes or next_palindromes or new_palindromes:
            for start, end in current_palindromes:
                if start-1 >= 0 and end+1 <= max_index and s[start-1] == s[end+1]:
                    new_palindromes.append((start-1, end+1))
            if current_palindromes:
                longest_palindromes = current_palindromes
            current_palindromes = next_palindromes
            next_palindromes = new_palindromes
            new_palindromes = []

        # 取出最长的回文
        start, end = longest_palindromes[0]
        return s[start: end+1]
