# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        if s.isspace():
            return s
        result = ""
        for item in s.split(" ")[::-1]:
            result = result + item + " "
        return result.strip()

print(Solution().ReverseSentence("student. a am I"))
