# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        first, second = 0, len(array)-1
        while first < second < tsum:
            sum_of_s = array[first] + array[second]
            if sum_of_s < tsum:
                first += 1
            elif sum_of_s > tsum:
                second -= 1
            else:
                return [array[first], array[second]]
        return []


if __name__ == '__main__':
    print(Solution().FindNumbersWithSum([1,2,4,7,11,15], 15))
