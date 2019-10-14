from collections import Counter

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.char_set = Counter()
        self.single_chars = []

    def FirstAppearingOnce(self):
        if self.single_chars:
            return self.single_chars[0]
        else:
            return '#'

    # write code here
    def Insert(self, char):
        count = self.char_set[char]
        if count > 1:
            return

        if count == 0:
            self.single_chars.append(char)
        elif count == 1:
            self.single_chars.remove(char)

        self.char_set.update(char)
