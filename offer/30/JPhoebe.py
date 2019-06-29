# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res = array[0]
        for i in range(0, len(array)):
            max = array[i]
            temp_max = max
            for j in range(i+1, len(array)):
                temp_max = temp_max + array[j]
                if temp_max > max:
                    max = temp_max
            if max > res:
                res = max
        print(res)
        return res

Solution().findgreatestsumofsubarray([-2,-8,-1,-5,-9])
# Solution().findgreatestsumofsubarray([1,-2,3,10,-4,7,2,-5])
# Solution().findgreatestsumofsubarray([-1, 2, -2, -3, -4])
