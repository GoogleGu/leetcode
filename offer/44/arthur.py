# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        return " ".join(s.split(" ")[::-1])


if __name__ == '__main__':
    print(Solution().ReverseSentence("student. a am I"))