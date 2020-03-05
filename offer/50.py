import pysnooper


# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    @pysnooper.snoop()
    def duplicate(self, numbers, duplication):
        count = 0
        index = 0
        while count < len(numbers):
            count += 1
            new_index = numbers[index]
            if new_index == index:
                index += 1
                continue
            if numbers[index] == numbers[new_index]:
                duplication[0] = numbers[index]
                return True
            numbers[index], numbers[new_index] = numbers[new_index], numbers[index]

        return False


Solution().duplicate([2,4,3,1,4], [])