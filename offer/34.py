# -*- coding:utf-8 -*-
class Solution:

    def FirstNotRepeatingChar(self, s):
        positions = {chr(index): -1 for index in set(range(97, 123)).union(set(range(65, 91)))}

        for pos, char in enumerate(s):
            if positions.get(char) is not None:
                if positions[char] != -1:
                    del positions[char]
                else:
                    positions[char] = pos
            if not positions:
                return -1
        valid_positions = [pos for pos in positions.values() if pos != -1]
        return min(valid_positions) if valid_positions else -1


