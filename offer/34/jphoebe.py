# -*- coding:utf-8 -*-
from collections import OrderedDict

class Solution:
    def FirstNotRepeatingChar(self, s):
        count_temp = OrderedDict()
        index_temp = {}
        index = 0
        for i in s:
            contain = i in count_temp
            if not contain:
                count_temp[i] = 1
            elif contain and count_temp[i] and count_temp[i] == 1:
                count_temp[i] = count_temp[i] + 1
            if i not in index_temp:
                index_temp[i] = index
            index += 1
        for count_str in count_temp.keys():
            if count_temp[count_str] == 1:
                return index_temp[count_str]
        return -1

print(Solution().FirstNotRepeatingChar("google"))
print(Solution().FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp"))
