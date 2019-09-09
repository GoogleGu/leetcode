# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):

        if not numbers:
            return False

        min = max = None
        same = False
        hash_tmp = {}

        for num in numbers:
            ## 初始化临界值
            if min == None and num != 0:
                min = num
            if max == None and num != 0:
                max = num
            ## 是否有相同数字
            if num != 0 and hash_tmp.__contains__(num):
                same = True
                break
            hash_tmp[num] = 1
            ## 变更临界值
            if num != 0 and num > max:
                max = num
            if num != 0 and num < min:
                min = num
        if same:
            return False
        ## 判断区间
        section = max - min - 1
        if section > 3:
            return False
        return True


print(Solution().IsContinuous([1,0,0,1,0]))
