import pysnooper

# -*- coding:utf-8 -*-
class Solution:

    # @pysnooper.snoop()
    def Add(self, num1, num2):
        mask = 1
        sum = 0
        increment = 0
        for i in range(32):
            bin1 = (num1 >> i) & mask
            bin2 = (num2 >> i) & mask
            this_bit = (((bin1 ^ bin2 ^ increment) & mask) << i)
            sum = sum | this_bit
            increment = (bin1 & bin2) | (bin1 & increment) | (bin2 & increment)

        return sum if sum <= 0x7FFFFFFF else ~(sum ^ 0xFFFFFFFF)
