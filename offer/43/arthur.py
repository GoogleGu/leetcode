# -*- coding:utf-8 -*-
class Solution:

    def LeftRotateString(self, s, n):
        if not s:
            return s
        k = n % len(s)
        return s[k:] + s[:k]


if __name__ == '__main__':
    print(Solution().LeftRotateString("abcXYZdef", 3))
