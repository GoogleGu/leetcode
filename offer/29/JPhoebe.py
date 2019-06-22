# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        self.quick_sort(tinput, 0, len(tinput)-1)
        return tinput[:k]

    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]

        while low < high:
            while low < high and array[high] >= key:
                high -= 1
            array[low] = array[high]
            array[high] = key

            while low < high and array[low] <= key:
                low += 1
            array[high] = array[low]
            array[low] = key

        self.quick_sort(array, left, low - 1)
        self.quick_sort(array, low + 1, right)
