import re

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        pattern = r'^[+-]?\d*(\.\d+)?([Ee][-+]?\d+)?$'
        return re.match(pattern, s)
