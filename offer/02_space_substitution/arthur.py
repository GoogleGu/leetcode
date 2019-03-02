# -*- coding:utf-8 -*-
import re


class Solution:
    # s 源字符串

    @staticmethod
    def replace_space(s):
        """
        运行结果
        --------
        运行时间：22ms
        占用内存：5624k
        """
        replaced_chars = []
        for char in s:
            if char == ' ':
                replaced_chars.append("%20")
            else:
                replaced_chars.append(char)
        return ''.join(replaced_chars)

    @staticmethod
    def replace_space_by_regex(s):
        """
        运行结果
        --------
        运行结果：24ms
        占用内存：5740k
        """
        return re.sub(' ', '%20', s)
