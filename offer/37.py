# -*- coding:utf-8 -*-
import pysnooper


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0
        index = binary_search(data, k)
        if index is not None:
            max_index = len(data) - 1
            upper_bound = index + 1
            while upper_bound <= max_index and data[upper_bound] == k:
                upper_bound += 1
            lower_bound = index - 1
            while lower_bound >= 0 and data[lower_bound] == k:
                lower_bound -= 1
            count = upper_bound - lower_bound - 1
        return count


def binary_search(data, x):
    """
    在输入的data有序序列二分查找x，返回值为x的下标，如果没有找到则返回None
    假设输入是按升序排列的。
    """
    start = 0
    end = len(data) - 1

    while end - start >= 0:
        mid = (start + end) // 2
        if data[mid] == x:
            return mid
        elif data[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == '__main__':
    data = [3]
    print(binary_search(data, 3))




