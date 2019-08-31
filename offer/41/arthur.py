# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        sequences = []
        start, end = 1, 2
        while start < end < tsum:
            sum_of_s = (start+end) / 2.0 * (end-start+1)
            if sum_of_s < tsum:
                end += 1
            elif sum_of_s > tsum:
                start += 1
            else:
                end += 1
                sequences.append(list(range(start, end)))

        return sequences


if __name__ == '__main__':
    print(Solution().FindContinuousSequence(3))





