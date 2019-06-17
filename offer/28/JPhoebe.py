# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        result = {}
        for num in numbers:
            count = 0
            exist = result.__contains__(num)
            if exist:
                count = result[num]
            result[num] = count + 1

        for key, count in result.items():
            if count > length / 2:
                return key
        return 0
