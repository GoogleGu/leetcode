import math
class Solution:
    def FindContinuousSequence(self, tsum):
        # （2x+n）(n+1)/2 = tsum
        result = []
        for x in range(1, tsum):
            n = math.sqrt(math.pow(2 * x + 1, 2) / 4 + 2 * tsum - 2 * x) - x - 0.5
            if n.is_integer() and n >= 1:
                n = (int)(n)
                ## n是正整数
                temp = []
                for item in range(x, x+n+1):
                    temp.append(item)
                result.append(temp)
        return result

Solution().FindContinuousSequence(3)
