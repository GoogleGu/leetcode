# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):

        # Find the xor result of the whole array
        xor = 0
        for num in array:
            xor = num ^ xor

        # find the non zero bit
        index = 0
        while xor & 1 != 1:
            index += 1
            xor = xor >> 1

        # find the two numbers
        num1, num2 = 0, 0
        for num in array:
            if (num >> index) & 1 == 1:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num

        return num1, num2



